from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
inf = 1e12
dp = [[inf] * (n+1) for _ in range(k+1)]
for i in range(k+1):
    dp[i][1] = 0

#print(dp)
graph = [[] for _ in range(n + 1)]


# level이 k에 달할 때 까지는 3차원 값을 올려도 좋음.
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

# 미세 최적화
for i in graph:
    i.sort(key=lambda x: x[1])
#print(graph)

pq = []
heappush(pq, (0, 1, 0))
def dijkstra():

    while pq:
        weight, start_node, level = heappop(pq)
        #print(weight, start_node, level)
        #노드의 끝일 때
        if start_node == n:
            return weight

        #중복 탐색 방지
        if dp[level][start_node] < weight:
            continue

        for next_node, next_weight in graph[start_node]:
            total_weight = next_weight + weight
            if dp[level][next_node] > total_weight:
                dp[level][next_node] = total_weight
                heappush(pq, (total_weight, next_node, level))

            if level < k and dp[level+1][next_node] > weight:
                dp[level+1][next_node] = weight
                heappush(pq, (weight, next_node, level+1))

ans = dijkstra()
#print(dp)
print(ans)


