
n, m, r = map(int, input().split())

item_arr = [0] + list(map(int, input().split()))

INF = 1000
matrix = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(r):
    start, end, value = map(int, input().split())
    matrix[start][end] = value
    matrix[end][start] = value

for i in range(n):
    matrix[i][i] = 0

for k in range(1, n+1):
    for p in range(1, n+1):
        for q in range(1, n+1):
            matrix[p][q] = min(matrix[p][q], matrix[p][k] + matrix[k][q])

max_item = 0
for row in range(1,n+1):
    items = 0
    for c in range(1,n+1):
       if matrix[row][c] <= m:
            items += item_arr[c]
    if max_item < items:
        max_item = items

print(max_item)
