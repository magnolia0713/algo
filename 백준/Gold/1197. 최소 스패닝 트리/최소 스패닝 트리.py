
from heapq import heappush, heappop

def dijk():
    pq = []
    heappush(pq, (0, 1))
    full_cost = 0
    while pq:
        cost, node = heappop(pq)
        if not visited[node]:
            full_cost += cost
            visited[node] = True

            for (new_cost, new_node) in lines[node]:
                if not visited[new_node]:
                    heappush(pq, (new_cost, new_node))


    return full_cost



v, e = map(int, input().split())

lines = [[] for _ in range(v+1)]
for _ in range(e):
    s, e, value = map(int, input().split())
    lines[s].append((value, e))
    lines[e].append((value, s))
visited = [False] * (v+1)
visited[0] =True
print(dijk())