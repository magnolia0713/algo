from copy import deepcopy

# 회전 행렬
def org(matrix):
    matrix3 = deepcopy(matrix)
    return matrix3

def matrix90(matrix):
    matrix2 = matrix[::-1]
    matrix3 = list(map(list, zip(*matrix2)))
    return matrix3

def matrix180(matrix):
    matrix2 = matrix[::-1]
    matrix3 = list(matrix2[i][::-1] for i in range(N))
    return matrix3

def matrix270(matrix):
    matrix2 = list(matrix[i][::-1] for i in range(N))
    matrix3 = list(map(list, zip(*matrix2)))
    return matrix3

def gaming(matrix):
    matrix2 = deepcopy(matrix)

    for r in range(N):
        for c in range(N - 1):
            count_a = 1
            while c + count_a < N:
                if matrix2[r][c] == matrix2[r][c + count_a]:
                    matrix2[r][c] = matrix2[r][c] * 2
                    matrix2[r][c + count_a] = 0
                    break
                elif matrix2[r][c + count_a] == 0:
                    count_a += 1
                else:
                    break

        for c in range(N):
            if matrix2[r][c] == 0:
                count = 1
                while c + count < N:
                    if matrix2[r][c + count] != 0:
                        matrix2[r][c] = matrix2[r][c + count]
                        matrix2[r][c + count] = 0
                        break
                    else:
                        count += 1
    return matrix2

def check(matrix):
    # result = []
    # check1 = False
    # check2 = False
    run = False

    checking = matrix[0][0]
    for r in range(N):
        if run:
            break

        for c in range(N):
            if matrix[r][c] != checking:
                run = True
                break

    else:
        return [0]

    return[0,1,2,3]
    # for r in range(N):
    #     saving = -1
    #     for c in range(N):
    #         if matrix[r][c] != 0:
    #             if matrix[r][c] == saving:
    #                 check1 = True
    #                 break
    #             else:
    #                 saving = matrix[r][c]
    #     if check1:
    #         break
    #
    # for c in range(N):
    #     saving = -1
    #     for r in range(N):
    #         if matrix[r][c] != 0:
    #             if matrix[r][c] == saving:
    #                 check2 = True
    #                 break
    #             else:
    #                 saving = matrix[r][c]
    #     if check2:
    #         break
    #
    # if check1:
    #     result.extend([0, 2])
    # if check2:
    #     result.extend([1, 3])

    return result

def dfs(depth, matrix):
    global max_a

    if depth == 5:
        mini_max = 0
        for row in matrix:
            if mini_max < max(row):
                mini_max = max(row)
        if max_a < mini_max:
            max_a = mini_max

    else:
        result = check(matrix)
        for i in result:
            if i == 0:
                dfs(depth+1, gaming(org(matrix)))

            elif i == 1:
                dfs(depth+1, gaming(matrix90(matrix)))

            elif i == 2:
                dfs(depth+1, gaming(matrix180(matrix)))

            elif i == 3:
                dfs(depth+1, gaming(matrix270(matrix)))


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
max_a = 0
dfs(0, matrix)
print(max_a)