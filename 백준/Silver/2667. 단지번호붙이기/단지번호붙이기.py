def bfs():
    count = 1
    while basket:
        n, m = basket.pop()
        for dr, dc in dirs:
            nr = n + dr
            nc = m + dc
            if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == 1:
                matrix[nr][nc] = 0
                basket.append((nr,nc))
                count += 1

    return count

dirs = [(0,1),(1,0),(-1,0),(0,-1)]
N = int(input())
matrix = [list(map(int, list(input()))) for _ in range(N)]
total_a = []
for r in range(N):
    for c in range(N):
        if matrix[r][c] != 0:
            matrix[r][c] = 0
            basket = [(r,c)]
            total_a.append(bfs())
total_a.sort()
print(len(total_a), *total_a, sep='\n')