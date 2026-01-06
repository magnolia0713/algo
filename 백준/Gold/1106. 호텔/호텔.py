c, n = map(int, input().split())

candidate = [] # cost, score
min_cost = 100000
for i in range(n):
    candidate.append(list(map(int, input().split())))

dp = [100000] * (c+1)
dp[c] = 0
for i in range(n):
    cost, score = candidate[i]
    for j in range(c, 0, -1):
        if dp[j] == 100000:
            continue

        if j - score <= 0:
            min_cost = min(min_cost, dp[j] + cost)

        else:
            dp[j-score] = min(dp[j-score], dp[j] + cost)

print(min_cost)
