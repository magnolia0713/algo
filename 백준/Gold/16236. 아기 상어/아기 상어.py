from collections import deque

def bfs(x,y,size):
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    basket = deque([(x,y)])
    list_a = []

    while basket:
        len_a = len(basket)
        for _ in range(len_a):
            r, c = basket.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:

                    if matrix[nr][nc] == 0 or matrix[nr][nc] == size:
                        visited[nr][nc] = visited[r][c] + 1
                        basket.append((nr,nc))

                    elif size > matrix[nr][nc]:
                        list_a.append((nr,nc))
                        visited[nr][nc] = visited[r][c] + 1

        if list_a:
            list_b = sorted(list_a)
            return (list_b[0][0], list_b[0][1], visited[r][c])

    return (-1,-1,0)

dirs = [(-1,0),(0,-1),(0,1),(1,0)]
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

count = 0
check = False
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 9:
            shark = (r,c)
            matrix[r][c] = 0
            check = True
            break

    if check:
        break
day = 0
size = 2
mini_count = 0
while True:
    result = bfs(shark[0],shark[1],size)
    if result[2] != 0:
        day += result[2]
        mini_count += 1
        if mini_count >= size:
            size += 1
            mini_count = 0
        shark = (result[0],result[1])
        matrix[result[0]][result[1]] = 0

    else:
        print(day)
        break