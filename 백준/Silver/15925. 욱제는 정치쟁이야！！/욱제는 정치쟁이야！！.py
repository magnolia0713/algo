n, status = map(int, input().split())
# list에 넣고 스택처럼 관리하면 될 것 같음.

matrix = [list(map(int, input().split())) for _ in range(n)]
if status:
    for r in range(n):
        for c in range(n):
            matrix[r][c] = 1 - matrix[r][c]

#print(matrix)
basket = []
sum_list = [[0] * n for _ in range(2)]
for idx in range(n):
    #가로 합
    sum_list[0][idx] = sum(matrix[idx])
    if sum_list[0][idx] <= n//2:
        basket.append((0, idx))

    #세로 합
    col_sum = 0
    for r in range(n):
         col_sum += matrix[r][idx]
    sum_list[1][idx] = col_sum
    if col_sum <= n//2:
        basket.append((1, idx))

#print(basket)
while basket:
    is_col, idx = basket.pop()
    #열일 때
    if is_col:
        sum_list[1][idx] = 0
        for i in range(n):
            if matrix[i][idx]:
                matrix[i][idx] = 0
                sum_list[0][i] -= 1
                if sum_list[0][i] == n//2:
                    basket.append((0,i))

    # 행일 때
    else:
        sum_list[0][idx] = 0
        for i in range(n):
            if matrix[idx][i]:
                matrix[idx][i] = 0
                sum_list[1][i] -= 1
                if sum_list[1][i] == n//2:
                    basket.append((1,i))

total = sum(sum_list[0]) + sum(sum_list[1])

ans = 1 if not total else 0
print(ans)