from sys import stdin
input = stdin.readline

n = int(input())
cnt = 0

default_start, a = map(int, input().split())

n_list = [(default_start), (a)]

for i in range(1,n):
    a, b = map(int, input().split())
    n_list.append(b)
inf = 1e10
memo = [[inf] * n for _ in range(n)]
for i in range(n):
    memo[i][i] = 0
for p in range(1, n):
    for r in range(0, n-p):
        for k in range(p):
            memo[r][r+p] = min(memo[r][r+p], memo[r][r+k] + n_list[r] * n_list[r+k+1] * n_list[r+p+1] + memo[r+k+1][r+p])

# for i in memo:
#     print(*i)
print(memo[0][n-1])