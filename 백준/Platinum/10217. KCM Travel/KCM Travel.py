import sys
input = lambda : sys.stdin.readline().rstrip()

inf = float('inf')
input()
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(k):
    a, b, cost, time = map(int, input().split())
    graph[a].append((b, cost, time))

dp = [[inf for _ in range(n + 1)] for _ in range(m + 1)]
dp[0][1] = 0

for s in range(m + 1):
    for x in range(1, n + 1):
        if dp[s][x] != inf:
            for nx, cost, time in graph[x]:
                if s + cost <= m:
                    dp[s+cost][nx] = min(dp[s+cost][nx], dp[s][x] + time)

answer = min(dp[i][n] for i in range(m + 1))
print(answer if answer != inf else 'Poor KCM')