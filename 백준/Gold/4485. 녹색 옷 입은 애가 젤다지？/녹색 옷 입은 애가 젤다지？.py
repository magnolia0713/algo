

from heapq import heappush, heappop


def dijk():

    pq = []
    heappush(pq, (matrix[0][0], (0,0)))

    while pq:
        cost, (r, c) = heappop(pq)

        if memo[n-1][n-1] <= cost:
            break

        if memo[r][c] < cost:
            continue

        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < n:
                temp_cost = cost + matrix[nr][nc]

                if memo[nr][nc] > temp_cost:
                    memo[nr][nc] = temp_cost
                    heappush(pq, (temp_cost,(nr,nc)))

    return memo[n-1][n-1]

tc = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while True:
    n = int(input())
    if n == 0:
        break
    tc += 1
    matrix = [list(map(int, input().split())) for _ in range(n)]
    INF = 1e6
    memo = [[INF] * n for _ in range(n)]

    print(f"Problem {tc}: {dijk()}")
