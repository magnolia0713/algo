from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s, e = map(int, input().split())
teleport = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    teleport[x].append(y)
    teleport[y].append(x)

def bfs(start, end):
    if start == end:
        return 0

    basket = deque()
    basket.append(start)
    while basket:
        node = basket.popleft()
        if node > 1 and not visited[node-1]:
            visited[node-1] = visited[node] + 1
            if end == node-1:
                ans = visited[node-1]
                return ans
            basket.append(node-1)

        if  node < n and not visited[node+1]:
            visited[node+1] = visited[node] + 1
            if end == node+1:
                ans = visited[node+1]
                return ans

            basket.append(node+1)

        for nxt_node in teleport[node]:
            if not visited[nxt_node]:
                visited[nxt_node] = visited[node] + 1
                if end == nxt_node:
                    ans = visited[nxt_node]
                    return ans

                basket.append(nxt_node)

    else:
        ans = -1
    return ans

print(bfs(s, e))