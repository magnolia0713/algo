#빙고판 생성
matrix = [list(map(int, input().split())) for _ in range(5)]
#print(matrix)

# 번호 리스트 작성
number_list = []

for i in range(5):
    number_list.extend(map(int, input().split()))
    
#print(number_list)

break_sys = False
for num in number_list:
    if break_sys == True:
        break
    for col in range(5):
        if break_sys == True:
            break
        for row in range(5):
            if matrix[col][row] == num:
                matrix[col][row] = 0
                #맞았을 때 마다 check
                bingo = 0
                #가로
                for i in range(5):
                    if sum(matrix[i]) == 0:
                        bingo += 1
                matrix_tr = (list(zip(*matrix)))
                #세로
                for i in range(5):
                    if sum(matrix_tr[i]) == 0:
                        bingo += 1
                #대각선
                if (matrix[0][0]+matrix[1][1]+matrix[2][2]+matrix[3][3]+matrix[4][4]) == 0:
                    bingo += 1
                if (matrix[4][0]+matrix[3][1]+matrix[2][2]+matrix[1][3]+matrix[0][4]) == 0:
                    bingo += 1

                if bingo >= 3:
                    indexed = number_list.index(num)
                    print(indexed + 1)
                    break_sys = True
                    break

