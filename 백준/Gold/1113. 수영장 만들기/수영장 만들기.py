
def bfs():
    basket = []
    for r,c in default:
        if not check_table[r][c]:
            basket.append((r,c))

    while basket:

        p, q = basket.pop()
        check_table[p][q] = True

        for dp, dq in dirs:
            np = p + dp
            nq = q + dq
            if 0 <= np < n and 0 <= nq < m and not check_table[np][nq]:
                basket.append((np,nq))
                check_table[np][nq] = True

    cnt = 0
    for r in range(n):
        cnt += check_table[r].count(False)
    return cnt


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(n)]
check_table = [[False] * m for _ in range(n)]


default = []
for i in range(m):
    default.append((0,i))
    default.append((n-1,i))

for j in range(1,n-1):
    default.append((j,0))
    default.append((j,m-1))

tc = 0
for i in range(1,9):
    check_table = [[False] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if matrix[r][c] > i:
                check_table[r][c] = True
    tc += bfs()

print(tc)