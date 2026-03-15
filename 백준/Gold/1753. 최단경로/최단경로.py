
import heapq, sys

input = sys.stdin.readline

heappop = heapq.heappop
heappush = heapq.heappush

def dijkstra(start):

    basket = [(0,start)]
    memo[start] = 0


    while basket:
        cost, p = heappop(basket)

        for i in line_matrix[p]:
            value, key = i[0], i[1]

            temp = cost + value
            if temp < memo[key]:
                memo[key] = temp
                heappush(basket, (temp , key))

V, E = map(int, input().split())
K = int(input())
line_matrix = [[] for _ in range(V+1)]


for _ in range(E):
    u,v,w = map(int, input().split())
    line_matrix[u].append((w,v))

for i in range(V+1):
    line_matrix[i].sort()

memo = [100000000] * (V+1)

dijkstra(K)


for i in range(1, V+1):

    if memo[i] == 100000000:
        memo[i] = 'INF'
    else:
        memo[i] = str(memo[i])

print('\n'.join(memo[1:]))