import sys
M, N = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count_a = 0
for row in matrix:
    count_a += row.count(1)

dir = [(1,0), (-1,0), (0,1), (0,-1)]
basket = []
basket2 = []
count_z = 0
counter = 0
first = True

while True:
    if first:
        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 1:
                    basket.append((r, c))

    if not basket2 and not first:
        for row in matrix:
            count_z += row.count(0)
        if count_z == 0:
            print(counter - 1)
            break
        else:
            print(-1)
            break

    while basket2 or first:
        if first:
            if not basket:
                first = False
                break
            basket2 = basket.copy()
            basket.clear()
            first = False

        r, c = basket2.pop()
        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 0:
                matrix[nr][nc] = 1
                basket.append((nr, nc))

    basket2 = basket.copy()
    basket.clear()
    counter += 1