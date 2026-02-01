from collections import deque
from sys import stdin
input = stdin.readline
n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (n+1)
subtree_cnt = [1] * (n+1)
basket = deque()

for i in range(1, n+1):
    visited[i] = len(graph[i])
    if visited[i] == 1 and i != r:
        basket.append(i)

while basket:
    cur = basket.popleft()
    visited[cur] = 0

    for i in graph[cur]:
        if visited[i] > 0:
            visited[i] -= 1
            subtree_cnt[i] += subtree_cnt[cur]

            if visited[i] == 1 and i != r:
                basket.append(i)

for _ in range(q):
    print(subtree_cnt[int(input())])
