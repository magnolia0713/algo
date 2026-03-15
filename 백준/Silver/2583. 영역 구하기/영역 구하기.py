N, M ,K = map(int, input().split())
matrix = [[0] * M for _ in range(N)]

for _ in range(K):
    m1, n1, m2, n2 = map(int, input().split())
    for r in range(n1, n2):
        for c in range(m1, m2):
            matrix[r][c] = 1
dir = [(1,0), (-1,0), (0, 1), (0, -1)]
total_counter = []
for r in range(N):
    for c in range(M):
        if not matrix[r][c]:
            matrix[r][c] = 1
            count = 1
            basket = [(r, c)]
            while basket:
                r, c = basket.pop()
                for dr, dc in dir:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < M and not matrix[nr][nc]:
                        basket.append((nr, nc))
                        matrix[nr][nc] = 1
                        count += 1
            total_counter.append(count)

total_counter.sort()
print(len(total_counter))
print(*total_counter)