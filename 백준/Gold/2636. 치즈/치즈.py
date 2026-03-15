N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
time_mat = [[-1] * M for _ in range(N)]
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

zero_day = [(0,0)]
matrix[0][0] = -1

while zero_day:
    r, c = zero_day.pop()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 0:
            matrix[nr][nc] = -1
            zero_day.append((nr, nc))

basket = []
for r in range(N):
    for c in range(M):
        if matrix[r][c] == -1:
            count_a = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 1:
                    count_a += 1

            if count_a > 0:
                time_mat[r][c] = 0
                basket.append((r,c))
day_a = 0
basket2 = []
check_point = [[True] * M for _ in range(N)]
while basket:
    n, m = basket.pop()
    for i in range(4):
        nr = n + dr[i]
        nc = m + dc[i]
        if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 1:
            matrix[nr][nc] = 0
            time_mat[nr][nc] = time_mat[n][m] + 1
            basket2.append((nr, nc))
            basket3 = [(nr,nc)]
            while basket3:
                p, q = basket3.pop()
                for k in range(4):
                    np = p + dr[k]
                    nq = q + dc[k]
                    if 0 <= np < N and 0 <= nq < M and matrix[np][nq] == 0 and time_mat[np][nq] == -1:
                        basket2.append((np, nq))
                        time_mat[np][nq] = time_mat[nr][nc]
                        check_point[np][nq] = False
                        basket3.append((np, nq))

    if not basket:
        basket = basket2.copy()
        basket2.clear()
        day_a += 1

sum_a = 0
print(day_a - 1)
count = 0
for r in range(N):
    for c in range(M):
        if time_mat[r][c] == day_a - 1 and check_point[r][c]:
            count += 1

print(count)