
n = int(input())

buildings = []
for _ in range(n):
    a, b = map(int, input().split())
    buildings.append((a, b))

buildings.sort()
memo = [0] * (buildings[n-1][0]+1)
default = 0
temp = buildings[0][0]
for i in range(n):
    for j in range(temp, buildings[i][0]):
        memo[j] = default

    default = max(default, buildings[i][1])
    temp = buildings[i][0]

else:
    memo[buildings[n-1][0]] = default

default = 0
temp = buildings[n-1][0]
for p in range(n-1,-1,-1):
    for q in range(temp, buildings[p][0], -1):
        memo[q] = (min(default, memo[q]))

    default = max(default, buildings[p][1])
    temp = buildings[p][0]

else:
    memo[buildings[0][0]] = (min(default,memo[buildings[0][0]]))

print(sum(memo))
