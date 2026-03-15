from copy import deepcopy
def dfs(depth, matrix_org):
    global min_a

    if depth == len(camera_a):
        count = 0
        for r in range(N):
            for c in range(M):
                if matrix_org[r][c] == 0:
                    count += 1
        if min_a > count:
            min_a = count
        return

    p, q, k = camera_a[depth]
    if k == 1:

        for i in range(4):
            matrix = deepcopy(matrix_org)
            for dist in range(8):
                nr = p + dir_r[i] * dist
                nc = q + dir_c[i] * dist
                if nr < 0 or nr >= N or nc < 0 or nc >= M or matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7

            dfs(depth+1, matrix)

    if k == 2:

        for j in range(4):
            matrix = deepcopy(matrix_org)
            for i in [j, (j+2)%4]:
                for dist in range(8):
                    nr = p + dir_r[i] * dist
                    nc = q + dir_c[i] * dist
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or matrix[nr][nc] == 6:
                        break
                    else:
                        if matrix[nr][nc] == 0:
                            matrix[nr][nc] = 7

            dfs(depth+1, matrix)

    if k == 3:

        for j in range(4):
            matrix = deepcopy(matrix_org)
            for i in [j, (j+1)%4]:
                for dist in range(8):
                    nr = p + dir_r[i] * dist
                    nc = q + dir_c[i] * dist
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or matrix[nr][nc] == 6:
                        break
                    else:
                        if matrix[nr][nc] == 0:
                            matrix[nr][nc] = 7

            dfs(depth+1, matrix)

    if k == 4:

        for j in range(4):
            matrix = deepcopy(matrix_org)
            for i in [j, (j+1)%4, (j+2)%4]:
                for dist in range(8):
                    nr = p + dir_r[i] * dist
                    nc = q + dir_c[i] * dist
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or matrix[nr][nc] == 6:
                        break
                    else:
                        if matrix[nr][nc] == 0:
                            matrix[nr][nc] = 7

            dfs(depth+1, matrix)

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
camera_a = []
camera_b = []
for r in range(N):
    for c in range(M):
        if 0 < matrix[r][c] < 5:
            camera_a.append((r,c, matrix[r][c]))

        elif matrix[r][c] == 5:
            camera_b.append((r,c))

for n, m in camera_b:
    for i in range(4):
        for dist in range(max(N,M)):
            nn = n + dir_r[i] * dist
            nm = m + dir_c[i] * dist
            if 0 <= nn < N and 0 <= nm < M:
                if matrix[nn][nm] == 6:
                    break
                elif matrix[nn][nm] == 0:
                    matrix[nn][nm] = 7
num = len(camera_a)

min_a = 64

dfs(0, matrix)
print(min_a)