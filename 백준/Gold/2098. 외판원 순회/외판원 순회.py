n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
memo = [[INF] * (1 << n) for _ in range(n)]
memo[0][1] = 0

for visited in range(1 << n):
    for start in range(n):
        if not (visited & (1 << start)):
            continue
        for i in range(n):
            if visited & (1 << i):
                continue
            if matrix[start][i] == 0:
                continue
            next_visited = visited | (1 << i)
            memo[i][next_visited] = min(memo[i][next_visited], memo[start][visited] + matrix[start][i])

ans = INF
for i in range(n):
    if matrix[i][0]:
        ans = min(ans, memo[i][(1 << n) - 1] + matrix[i][0])

print(ans)