
from collections import deque

n = int(input())
tree = {}
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    start, end = map(int, input().split())
    tree.setdefault(start, []).append(end)

    graph[end].append(start)
    graph[start].append(end)

basket = deque()
for i in range(n+1):
    if len(graph[i]) == 1:
        basket.append(i)

memo = [0] * (n+1)

while basket:
    node = basket.popleft()
    if not memo[node]:
        memo[graph[node][0]] = 1
        graph[graph[node][0]].remove(node)

        if len(graph[graph[node][0]]) == 1:
            basket.append(graph[node][0])
        elif len(graph[graph[node][0]]) == 0:
            break

    else:
        graph[graph[node][0]].remove(node)

        if len(graph[graph[node][0]]) == 1:
            basket.append(graph[node][0])
        elif len(graph[graph[node][0]]) == 0:
            break

memo[0] = 0
print(sum(memo))