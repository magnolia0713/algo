N = int(input())

def dfs(r, c):
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and check_point[nr][nc] and matrix[nr][nc] == 1:
            check_point[nr][nc] = False
            counter[0] += 1
            dfs(nr, nc)
    else: return

#for dfs
matrix = [list(map(int, list(input()))) for _ in range(N)]
check_point = [[True] * N for _ in range(N)]
dir = [(1,0),(0,1),(0,-1),(-1,0)]
list_temp = []
list_size = []
for r in range(N):
    for c in range(N):
        if check_point[r][c] and matrix[r][c] == 1:
            check_point[r][c] = False
            counter = [1]
            dfs(r,c)
            if counter[0] != 0:
                list_size.append(counter[0])
        else:
            check_point[r][c] = False

list_size.sort()
print(len(list_size))
print(*list_size, sep='\n')