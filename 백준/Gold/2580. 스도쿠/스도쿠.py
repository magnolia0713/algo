from copy import deepcopy
def correcting():
    check = True

    while check:
        check = False

        for r in range(9):
            mini_count = 0
            mini_sum = 0
            for c in range(9):
                if matrix[r][c] == 0:
                    mini_count += 1
                    p, q = r, c
                mini_sum += matrix[r][c]

            if mini_count == 1:
                matrix[p][q] = 45 - mini_sum
                check = True

            # 세로
            for c in range(9):
                mini_count = 0
                mini_sum = 0
                for r in range(9):
                    if matrix[r][c] == 0:
                        mini_count += 1
                        p, q = r, c
                    mini_sum += matrix[r][c]

                if mini_count == 1:
                    matrix[p][q] = 45 - mini_sum
                    check = True

            if mini_count == 1:
                matrix[r][c] = 45 - mini_sum

            for dr in range(0, 9, 3):
                for dc in range(0, 9, 3):
                    mini_count = 0
                    mini_sum = 0
                    for r in range(3):
                        for c in range(3):
                            if matrix[r + dr][c + dc] == 0:
                                mini_count += 1
                                p, q = r + dr, c + dc
                            mini_sum += matrix[r + dr][c + dc]

                    if mini_count == 1:
                        matrix[p][q] = 45 - mini_sum
                        check = True



def dfs(depth):
    global check2, result

    if check2:
        return

    if depth == remains:
        result = deepcopy(matrix)
        check2 = True
        return

    n,m = basket[depth]
    num_set = {1,2,3,4,5,6,7,8,9}
    for r in range(9):
        if matrix[r][m] in num_set:
            num_set -= {matrix[r][m]}

    for c in range(9):
        if matrix[n][c] in num_set:
            num_set -= {matrix[n][c]}

    for r in range(n-n%3,n-n%3+3):
        for c in range(m-m%3,m-m%3+3):
            if matrix[r][c] in num_set:
                num_set -= {matrix[r][c]}
    a_tuple = tuple(num_set)
    if num_set:
        for k in a_tuple:
            matrix[n][m] = k
            dfs(depth+1)
            matrix[n][m] = 0
            basket.append

    else:
        return

matrix = [list(map(int, input().split())) for _ in range(9)]
basket = []

correcting()

for r in range(9):
    for c in range(9):
        if matrix[r][c] == 0:
            basket.append((r,c))

if not basket:
    for i in matrix:
        print(*i)


else:
    result = []
    check2 = False
    remains = len(basket)
    dfs(0)
    for i in result:
        print(*i)