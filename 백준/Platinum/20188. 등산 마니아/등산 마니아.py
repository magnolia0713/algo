from sys import stdin
from collections import deque
input = stdin.readline

def tracing():
    while basket:
        p = basket.popleft()

        for i in graph[p]:
            if lines[i]:
                lines[i] -= 1
                if not lines[i]:
                    basket.append(i)
            else:
                memo[p] += memo[i] + 1

n = int(input())
memo = [0] * (n+1)
graph = [[] for _ in range(n+1)]
lines = [-1] * (n+1)
lines[1] = -500000
dist = [-1] * (n+1)
dist[1] = 0

def treeing():
    res = 0
    basket2 = deque([1])

    while basket2:
        k = basket2.popleft()
        for i in graph[k]:
            if dist[i] == -1:
                dist[i] = dist[k] + 1
                res += dist[i]
                basket2.append(i)

    return res * (n-1)




for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    lines[a] += 1 ; lines[b] += 1



result = treeing()

basket = deque()
for i in range(2, n+1):
    if not lines[i]:
        basket.append(i)

minus = 0
tracing()

for p in range(2,n+1):
    i = memo[p]
    minus += (i+1) * i // 2
print(result - minus)