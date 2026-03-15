num = int(input())
case_num = int(input())
matrix = [list(map(int, input().split())) for _ in range(case_num)]
number_list = [1]

for x in number_list:
    for i in range(case_num):
        for j in range(2):
            if matrix[i][j] == x:
                if matrix[i][1-j] not in number_list:
                    number_list.append(matrix[i][1-j])

print(len(number_list)-1)