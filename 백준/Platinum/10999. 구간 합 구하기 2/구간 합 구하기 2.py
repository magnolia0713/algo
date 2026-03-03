import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# n개의 수를 통해 세그트리 구성 (lazy 관리 tree도 생성)
temp = (n-1).bit_length()
added_length = 2 ** temp
seg_tree = [0] * (added_length * 2)
lazy_tree = [0] * (added_length * 2)
#print(len(seg_tree)) # 넉넉하게 더미노드까지 생성

# 주의: 1번 노드는 idx added_length 0번부터 시작

for i in range(n):
    num = int(input())
    seg_tree[added_length + i] = num

for i in range(added_length-1, 0, -1):
    seg_tree[i] = seg_tree[2*i] + seg_tree[2*i+1]

# 구간합 수정
def query1(node, s, e, L, R, num):

    # 경계조건이 아예 맞지 않을 때
    if e <= L or s >= R:
        return

    # 범위가 경계안에 완전히 포함될 때
    if s <= L and e >= R:
        seg_tree[node] += num * (R-L)
        lazy_tree[node] += num
        return

    # 범위가 걸쳐져 있을 때 (재귀 구현)

    # push 함수 구현이 필요해 보이는데.....(lazy node 처리 함수)
    # push 함수를 한 번 풀어서 구현해보자.
    leaf = node * 2
    seg_tree[leaf] += lazy_tree[node] * ((R - L)//2)
    seg_tree[leaf+1] += lazy_tree[node] * ((R - L)//2)
    lazy_tree[leaf] += lazy_tree[node]
    lazy_tree[leaf+1] += lazy_tree[node]
    lazy_tree[node] = 0
    mid = (L+R)//2
    # 재귀
    query1(leaf, s, e, L, mid, num)
    query1(leaf+1, s, e, mid, R, num)

    # 재귀 결과를 본 후에 tree node 갱신
    seg_tree[node] = seg_tree[leaf] + seg_tree[leaf+1]
    return

# 구간합 출력
# query2 를 위한 재귀 구현
def recursion(node, s, e, L, R):
    global ans
    # 범위 밖
    if s >= R or e <= L:
        return

    # 범위 완전 포함
    if s <= L and e >= R:
        ans += seg_tree[node]
        return

    # 범위 부분 포함
    leaf = node * 2
    seg_tree[leaf] += lazy_tree[node] * ((R - L)//2)
    seg_tree[leaf+1] += lazy_tree[node] * ((R - L)//2)
    lazy_tree[leaf] += lazy_tree[node]
    lazy_tree[leaf+1] += lazy_tree[node]
    lazy_tree[node] = 0
    mid = (L+R)//2
    # 재귀
    recursion(leaf, s, e, L, mid)
    recursion(leaf+1, s, e, mid, R)

    # 재귀 결과를 본 후에 tree node 갱신
    seg_tree[node] = seg_tree[leaf] + seg_tree[leaf+1]
    return


def query2(node, s, e, L, R):
    global ans
    ans = 0
    recursion(node, s, e, L, R)

    return ans


# print(seg_tree)
# print(lazy_tree)

#query 처리
for _ in range(m+k):
    query = list(map(int, input().split()))
    # query 1
    if len(query) == 4:
        _, start, end, num = query

        # 바로 재귀 수행
        query1(1, start-1 , end , 0, added_length, num)
        #print(seg_tree)
    # query 2
    else:
        _, start, end = query

        # 답만 구하면 되는 상황. lazy node만 처리하면 끝.
        print(query2(1, start-1, end, 0, added_length))