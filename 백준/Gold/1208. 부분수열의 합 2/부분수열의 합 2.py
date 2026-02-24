import sys
input = sys.stdin.readline

def gen_sums(arr):
    res = []
    def dfs(idx, acc):
        if idx == len(arr):
            res.append(acc)
            return
        dfs(idx + 1, acc)            # 안 고름
        dfs(idx + 1, acc + arr[idx]) # 고름
    dfs(0, 0)
    return res

n, s = map(int, input().split())
n_list = list(map(int, input().split()))
m_list = n_list[:n//2]
p_list = n_list[n//2:]

a_list = gen_sums(m_list)
b_list = gen_sums(p_list)

a_list.sort()
b_list.sort()

head, tail = 0, len(b_list) - 1
ans = 0

while head < len(a_list) and tail >= 0:
    cur = a_list[head] + b_list[tail]
    if cur < s:
        head += 1
    elif cur > s:
        tail -= 1
    else:
        cnt_a = 1
        cnt_b = 1
        while head < len(a_list) - 1 and a_list[head] == a_list[head + 1]:
            cnt_a += 1
            head += 1
        while tail > 0 and b_list[tail] == b_list[tail - 1]:
            cnt_b += 1
            tail -= 1
        ans += cnt_a * cnt_b
        head += 1
        tail -= 1

if s == 0:
    ans -= 1  # 공집합 제거(BOJ 1208)

print(ans)