n, m = map(int, input().split())

INF = 100000
matrix = [[INF] * (n+1) for _ in range(n+1)]

#거리 매트릭스 정렬
for _ in range(m):
    a, b, c = map(int, input().split())

    matrix[a][b] = c

for i in range(1, n+1):
    matrix[i][i] = 0

#플로이드
for k in range(1, n+1):
    for r in range(1, n+1):
        for c in range(1, n+1):
            matrix[r][c] = min(matrix[r][c], matrix[r][k] + matrix[k][c])

#친구집 색인
num_friend = int(input())
home_arr = list(map(int, input().split()))
a_min = 100000
for i in range(1, n+1):
    mini_sum = 0
    for j in home_arr:
        if matrix[i][j] != 100000 and matrix[j][i] != 100000:
            if mini_sum < matrix[j][i] + matrix[i][j]:
                mini_sum = matrix[j][i] + matrix[i][j]
        else:
            break

    if a_min > mini_sum:
        a_min = mini_sum
        final_arr = [i]

    elif a_min == mini_sum:
        final_arr.append(i)

print(*final_arr)