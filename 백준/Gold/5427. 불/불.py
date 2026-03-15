from collections import deque

def find():
    for r in range(N):
        for c in range(M):

            if matrix[r][c] == '*':
                fire_basket.append((r,c))

            elif matrix[r][c] == '@':
                person = (r, c)

    return person

def bfs(person):
    basket = deque([person])
    while basket:
        len_z = len(fire_basket)
        for _ in range(len_z):
            n, m = fire_basket.popleft()
            for dn, dm in dirs:
                nn = n + dn
                nm = m + dm
                if 0 <= nn < N and 0 <= nm < M and (matrix[nn][nm] == '.' or matrix[nn][nm] == '@'):
                    matrix[nn][nm] = '*'
                    fire_basket.append((nn,nm))

        len_a = len(basket)
        for _ in range(len_a):
            r, c = basket.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0<= nc < M and matrix[nr][nc] == '.' and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    basket.append((nr,nc))
                    if nr == 0 or nr == N-1 or nc == 0 or nc == M-1:
                        return visited[nr][nc] + 1

    return 'IMPOSSIBLE'

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
T = int(input())

for _ in range(T):
    M, N = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    fire_basket = deque()
    visited = [[-1] * M for _ in range(N)]
    person = find()
    if person[0] == 0 or person[0] == N-1 or person[0] == 0 or person[1] == M-1:
        print(1)
    else:
        visited[person[0]][person[1]] = 0
        result = bfs(person)
        print(result)