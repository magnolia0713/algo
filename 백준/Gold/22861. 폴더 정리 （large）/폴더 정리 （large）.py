from collections import deque

a, b = map(int, input().split())

# 트리는 "이름"을 담는 set (폴더/파일 모두)
tree = [set() for _ in range(a + 1)]

# folder_name -> (parent_idx, my_idx)
pointer_storage = {'main': (-1, 0)}
pointer = 0

# idx -> folder_name (postorder 재생성/디버깅용)
idx_to_name = [''] * (a + 1)
idx_to_name[0] = 'main'

# ---------- 1) 입력을 먼저 저장 (org가 나중에 나와도 KeyError 방지) ----------
children = {}  # org_name -> list of (name, isfolder)
for _ in range(a + b):
    org, name, isfolder = input().split()
    children.setdefault(org, []).append((name, isfolder))

# ---------- 2) main부터 내려가며 폴더에 인덱스 부여 + tree 채우기 ----------
q = deque(['main'])
while q:
    org = q.popleft()
    org_idx = pointer_storage[org][1]

    for name, isfolder in children.get(org, []):
        tree[org_idx].add(name)

        if isfolder == '1' and name not in pointer_storage:
            pointer += 1
            pointer_storage[name] = (org_idx, pointer)
            idx_to_name[pointer] = name
            q.append(name)

# ---------- 3) 이동 연산 ----------
c = int(input())
for _ in range(c):
    parent, child = input().split()
    ance = parent.split('/')[-2]
    p = parent.split('/')[-1]
    ch = child.split('/')[-1]

    p_idx = pointer_storage[p][1]
    ch_idx = pointer_storage[ch][1]

    # p 안의 모든 자식(파일/폴더)을 ch로 옮김(합치기)
    for j in list(tree[p_idx]):  # 안전하게 list로
        if j in pointer_storage:  # 폴더면 부모 idx 갱신
            pointer_storage[j] = (ch_idx, pointer_storage[j][1])
        tree[ch_idx].add(j)

    tree[p_idx].clear()
    tree[pointer_storage[ance][1]].discard(p)  # ance에서 p 제거(폴더 삭제)

# ---------- 4) (핵심) 이동 후 최종 트리 기준 postorder 재생성 ----------
orders = deque()
root = 0  # main idx

stack = [(root, 0)]  # (idx, state) state: 0=enter, 1=exit
while stack:
    idx, state = stack.pop()
    if state == 0:
        stack.append((idx, 1))
        for name in tree[idx]:
            if name in pointer_storage:  # 자식 폴더만 내려감
                stack.append((pointer_storage[name][1], 0))
    else:
        orders.append(idx_to_name[idx])

# ---------- 5) 폴더별 파일 종류 수 / 전체 파일 수 DP ----------
set_counter = [set() for _ in range(a + 1)]
total_counter = [0] * (a + 1)

d = int(input())

for folder_name in orders:
    idx = pointer_storage[folder_name][1]
    for name in tree[idx]:
        if name in pointer_storage:  # 자식 폴더
            cidx = pointer_storage[name][1]
            set_counter[idx] |= set_counter[cidx]
            total_counter[idx] += total_counter[cidx]
        else:  # 파일
            set_counter[idx].add(name)
            total_counter[idx] += 1

# ---------- 6) 질의 ----------
for _ in range(d):
    target = input().split('/')[-1]  # 폴더 이름(유일)
    t = pointer_storage[target][1]
    print(len(set_counter[t]), total_counter[t])
