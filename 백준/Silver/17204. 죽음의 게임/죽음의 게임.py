from collections import deque
n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[int(input())].append(i)

#print(graph)
visited = [0] * n
cnt = 0

def bfs():
    temp = set()

    for i in range(n):
        for j in temp:
            basket.append(j)
        temp.clear()
        for _ in range(len(basket)):
            node = basket.popleft()
            for p in graph[node]:
                if p == 0:
                    return i + 1

                temp.add(p)
    return -1

basket = deque()
basket.append(k)
ans = bfs()

print(ans)
