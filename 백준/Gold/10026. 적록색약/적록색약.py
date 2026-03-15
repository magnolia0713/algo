import sys
sys.setrecursionlimit(100000)

def dfs(r, c):
    check_list[r][c] = False
    if color == matrix[r][c]:
        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == color and check_list[nr][nc]:
                dfs(nr,nc)
    return

N = int(input())
matrix = [list(input()) for _ in range(N)]
check_list = [[True] * N for _ in range(N)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
counter_a = 0
#정상인
for r in range(N):
    for c in range(N):
        color = matrix[r][c]
        if check_list[r][c]:
            dfs(r,c)
            counter_a += 1
print(counter_a, end=' ')
#색약
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 'G':
            matrix[r][c] = 'R'

check_list = [[True] * N for _ in range(N)]
counter_b = 0

for r in range(N):
    for c in range(N):
        color = matrix[r][c]
        if check_list[r][c]:
            dfs(r,c)
            counter_b += 1
print(counter_b)