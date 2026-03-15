from collections import deque
import sys
N, M = map(int, input().split())
matrix = [list(sys.stdin.readline().strip()) for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_a = 0
for r in range(N):
    for c in range(M):
        if r-1 >= 0 and r+1 < N and  c-1 >= 0 and c+1 < M:
            min_counter = 0
            if matrix[r+1][c] == 'L':
                min_counter +=1
            if matrix[r-1][c] == 'L':
                min_counter +=1
            if matrix[r][c+1] == 'L':
                min_counter +=1
            if matrix[r][c-1] == 'L':
                min_counter +=1
            if min_counter > 2:
                continue

        if matrix[r][c] == 'L':
            basket = deque([(r, c)])
            distance = [[-1] * M for _ in range(N)]
            distance[r][c] = 0
            while basket:
                    n, m = basket.popleft()
                    for dr, dc in dir:
                        nr = n + dr
                        nc = m + dc

                        if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 'L' and distance[nr][nc] == -1:
                            basket.append((nr, nc))
                            distance[nr][nc] = distance[n][m] + 1
                            if distance[nr][nc] > max_a:
                                max_a = distance[nr][nc]

print(max_a)