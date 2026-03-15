
def dfs(depth, r, c):
    global a_max

    if a_max == counts:
        return

    if depth >= counts:
        a_max = counts
        return

    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < n and 0 <= nc < m and not visited[matrix[nr][nc]]:
            visited[matrix[nr][nc]] = True
            dfs(depth + 1, nr, nc)
            visited[matrix[nr][nc]] = False

        else:
            if a_max < depth:
                a_max = depth



dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
a_max = 0
visited = [False] * 26
sets = set()
for r in range(n):
    for c in range(m):
        matrix[r][c] = ord(matrix[r][c]) - 65
        sets.add(matrix[r][c])

counts = len(sets)
visited[matrix[0][0]] = True
dfs(1, 0, 0)

print(a_max)
