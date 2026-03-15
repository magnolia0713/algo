
def dfs(start, value):
    global a_min
    if not visit_list:
        if a_min > value:
            a_min = value
        return

    if n == check:
        count = 0
        for i in visit_list:
            count += min_list[i]

        if value + count > a_min:
            return

    for p in range(len(visit_list)):
        q = visit_list.pop(p)
        dfs(q, value + matrix[start][q])
        visit_list.insert(p,q)


n, m = map(int, input().split())
check = n // 3 * 2
INF = 10000000

matrix = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for r in range(n):
        for c in range(n):
            matrix[r][c] = min(matrix[r][c], matrix[r][k] + matrix[k][c])

min_list = []
for i in range(n):
    matrix[i][i] = 1000000
    min_list.append(min(matrix[i]))


for i in range(n-2,-1,-1):
    min_list[i] += min_list[i+1]

visit_list = list(range(n))
visit_list.remove(m)
a_min = 10000000
dfs(m,0)

print(a_min)