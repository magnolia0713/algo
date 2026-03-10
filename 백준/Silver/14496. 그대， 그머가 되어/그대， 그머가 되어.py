from collections import deque
st, en = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (n+1)
#print(graph)
basket = deque()
basket.append(st)


def bfs():
	cnt = 0
	while basket:
		#print(basket)
		for _ in range(len(basket)):
			node = basket.popleft()

			if node == en:
				ans = cnt
				return cnt

			for nxt_node in graph[node]:
				if not visited[nxt_node]:
					visited[nxt_node] = 1
					basket.append(nxt_node)
		cnt += 1
	return -1

print(bfs())