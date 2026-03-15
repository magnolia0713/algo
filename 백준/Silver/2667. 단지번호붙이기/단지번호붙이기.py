N = int(input())
matrix = [list(map(int, list(input()))) for _ in range(N)]
check_list = []
list_a = []
list_size = []
matrix_visited = [[True] * N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if matrix[r][c] == 1 and [r,c] and matrix_visited[r][c]:
            list_a.append([r,c])
            matrix_visited[r][c] = False

            for i, j in list_a:
                for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 1 and matrix_visited[ni][nj]:
                        list_a.append([ni,nj])
                        matrix_visited[ni][nj] = False
            check_list.extend(list_a.copy())
            list_size.append(len(list_a))
            list_a.clear()
list_size.sort()
print(len(list_size))
print(*list_size, sep='\n')