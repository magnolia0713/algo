from collections import deque

def bfs():
    basket = deque([(0,0)])

    while basket:
        n,m = basket.popleft()
        if n == N-1 and m == M-1:
            return distance[n][m]

        for dr, dc in dirs:
            nn = n + dr
            nm = m + dc
            if 0 <= nn < N and 0 <= nm < M and matrix[nn][nm] == 1 and distance[nn][nm] == -1:
                basket.append((nn,nm))
                distance[nn][nm] = distance[n][m] + 1

N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]
distance = [[-1] * M for _ in range(N)]
distance[0][0] = 1
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
result = bfs()
print(result)