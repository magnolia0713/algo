from collections import deque
n, min_a, max_a = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(r, c):
    basket = deque([(r, c)])
    teams = [(r, c)]
    visited[r][c] = 1

    while basket:
        p, q = basket.popleft()
        for dp, dq in dirs:
            np = p + dp
            nq = q + dq
            if 0 <= np < n and 0 <= nq < n and not visited[np][nq] and min_a <= abs(matrix[np][nq] - matrix[p][q]) <= max_a:
                visited[np][nq] = 1
                basket.append((np, nq))
                teams.append((np, nq))

    return teams

n_square = n * n
day = 0
while True:
    visited = [[0] * n for _ in range(n)]
    union = []
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                result = (bfs(r, c))
                if len(result) != 1:
                    union.append(result)

    if union:
        for unions in union:
            sub_sum = 0
            for a, b in unions:
                sub_sum += matrix[a][b]
            temp = sub_sum // len(unions)

            for a, b in unions:
                matrix[a][b] = temp

        day += 1

    else:
        print(day)
        break