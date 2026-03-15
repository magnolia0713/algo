from copy import deepcopy
def dfs1(depth, matrix, start):
    global max_a
    if max_a < depth:
        max_a = depth

    for r in range(start//N, N):
        for c in range(r % 2, N, 2):
            if not matrix[r][c]:
                matrix[r][c] = 1
                basket.add((r,c))

                visited2 = deepcopy(matrix)

                for n, m in basket:
                    for dn, dm in dirs:
                        for dist in range(1, N+1):
                            nn = n + dn * dist
                            nm = m + dm * dist
                            if nn < 0 or nm < 0 or nn >= N or nm >= N:
                                break

                            elif matrix[nn][nm] == 0:
                                visited2[nn][nm] = 2

                dfs1(depth + 1, visited2, r*N+c+1)
                matrix[r][c] = 0
                basket.remove((r,c))

def dfs2(depth, matrix, start):
    global max_b
    if max_b < depth:
        max_b = depth


    for r in range(start // N, N):
        for c in range((r+1) % 2, N, 2):
            if not matrix[r][c]:
                matrix[r][c] = 1
                basket.add((r, c))

                visited2 = deepcopy(matrix)

                for n, m in basket:
                    for dn, dm in dirs:
                        for dist in range(1, N + 1):
                            nn = n + dn * dist
                            nm = m + dm * dist
                            if nn < 0 or nm < 0 or nn >= N or nm >= N:
                                break

                            elif matrix[nn][nm] == 0:
                                visited2[nn][nm] = 2

                dfs2(depth + 1, visited2, r * N + c + 1)
                matrix[r][c] = 0
                basket.remove((r, c))

dirs = [(1,1),(-1,1),(1,-1),(-1,-1)]
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
for r in range(N):
    for c in range(N):
        matrix[r][c] = 1 - matrix[r][c]

if N == 1:
    print(1)

else:
    edge_case1 = sum(matrix[0]) + sum(matrix[N-1])
    if edge_case1 < 2:
        print(2*N-2)

    else:
        max_a = 0
        max_b = 0
        basket = set()
        dfs1(0,matrix,0)
        dfs2(0,matrix,0)
        print(max_a + max_b)