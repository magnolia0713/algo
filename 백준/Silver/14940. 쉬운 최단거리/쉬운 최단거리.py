from collections import deque
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
#print(matrix)

visited = [[0] * m for _ in range(n)]

basket = deque([])
check = False
for r in range(n):
    for c in range(m):
        if matrix[r][c] == 2:
            basket.append((r, c))
            visited[r][c] = 0
            check = True

    if check:
        break


dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
while basket:
    p, q = basket.popleft()

    for i in range(4):
        np = p + dir_r[i]
        nq = q + dir_c[i]

        if 0 <= np < n and 0 <= nq < m and matrix[np][nq] == 1 and not visited[np][nq]:
            visited[np][nq] = 1
            basket.append((np, nq))
            visited[np][nq] = visited[p][q] + 1

for r in range(n):
    for c in range(m):
        if matrix[r][c] == 1 and not visited[r][c]:
            visited[r][c] = -1

for i in visited:
    print(*i)