N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
edge_mat = []
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 1 and not visited[r][c]:
            visited[r][c] = 1
            subset = set()
            basket = [(r,c)]

            while basket:
                p, q = basket.pop()
                if (p+1 < N and matrix[p+1][q] == 0) or (p > 0 and matrix[p-1][q] == 0) or (q+1 < N and matrix[p][q+1] == 0) or (q>0 and matrix[p][q-1] == 0):
                    subset.add((p, q))

                for dp, dq in dirs:
                    np = p + dp
                    nq = q + dq
                    if 0 <= np < N and 0 <= nq < N and matrix[np][nq] and not visited[np][nq]:
                        basket.append((np,nq))
                        visited[np][nq] = 1

            edge_mat.append(subset)

min_a = 200
for n in range(len(edge_mat)):
    for m in range(n+1, len(edge_mat)):
        for r, c in edge_mat[n]:
            for x, y in edge_mat[m]:
                if min_a > abs(r-x) + abs(c-y):
                    min_a = abs(r-x) + abs(c-y)
        if min_a == 2:
            break

print(min_a -1)