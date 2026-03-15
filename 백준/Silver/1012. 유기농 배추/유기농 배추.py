T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]

    for _ in range(K):
        m, n = map(int, input().split())
        matrix[n][m] = 1

    dir = [(1,0), (-1,0), (0,1), (0,-1)]
    storage = []
    count = 0
    for r in range(N):
        for c in range(M):
            if matrix[r][c]:
                matrix[r][c] = 0
                storage.append((r, c))
                while storage:
                    n, m = storage.pop()
                    for dr, dc in dir:
                        nr = n + dr
                        nc = m + dc
                        if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc]:
                            matrix[nr][nc] = 0
                            storage.append((nr, nc))
                count += 1

    print(count)