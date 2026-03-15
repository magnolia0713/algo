from copy import deepcopy
N = int(input())
matrix_a = [list(map(int, input().split())) for _ in range(N)]
min_a = 100
max_a = 2
dir = [(1,0), (-1,0), (0,1), (0,-1)]
for r in range(N):
    for c in range(N):
        if min_a > matrix_a[r][c]:
            min_a = matrix_a[r][c]
        if max_a < matrix_a[r][c]:
            max_a = matrix_a[r][c]

max_count = 0
for num in range(0, max_a+1):
    matrix = deepcopy(matrix_a)
    for r in range(N):
        for c in range(N):
            if matrix[r][c] <= num:
                matrix[r][c] = 0

    count = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c]:
                basket = [(r,c)]
                matrix[r][c] = 0

                while basket:
                    n, m = basket.pop()
                    for dr, dc in dir:
                        nr = n + dr
                        nc = m + dc
                        if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc]:
                            basket.append((nr,nc))
                            matrix[nr][nc] = 0
                count += 1
    if max_count < count:
        max_count = count

print(max_count)