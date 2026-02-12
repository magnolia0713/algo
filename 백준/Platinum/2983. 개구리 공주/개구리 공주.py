from collections import defaultdict

n, k = map(int, input().split())
orders = list(input())

# 좌표를 받아오자.
coord = []
for i in range(n):
    coord.append(list(map(int, input().split())))

# 이제 x+y, x-y로 정렬해보자.
plus_dict = defaultdict(list)
minus_dict = defaultdict(list)

for i in range(n):
    x, y = coord[i][0], coord[i][1]
    plus_dict[x+y].append(((x-y),i))
    minus_dict[x-y].append(((x+y), i))

#++, +-. -+. --
arr_pointer = [[-1,-1,-1,-1] for _ in range(n)]

for plus_arr in plus_dict:
    plus_dict[plus_arr].sort()
    # ++ 방향
    for i in range(len(plus_dict[plus_arr])-1):
        arr_pointer[plus_dict[plus_arr][i][1]][0] = plus_dict[plus_arr][i+1][1]

    # +- 방향
    for i in range(1,len(plus_dict[plus_arr])):
        arr_pointer[plus_dict[plus_arr][i][1]][1] = plus_dict[plus_arr][i-1][1]

for minus_arr in minus_dict:
    minus_dict[minus_arr].sort()
    # -+ 방향
    for i in range(len(minus_dict[minus_arr])-1):
        arr_pointer[minus_dict[minus_arr][i][1]][2] = minus_dict[minus_arr][i+1][1]

    # -- 방향
    for i in range(1,len(minus_dict[minus_arr])):
        arr_pointer[minus_dict[minus_arr][i][1]][3] = minus_dict[minus_arr][i-1][1]

#_------------------------링크드 리스트(배열) 완성
# 시작 인덱스
idx = 0

# 개구리 점프 시작
for i in orders:
    #++ 방향
    if  i == 'B':
        if arr_pointer[idx][0] != -1:

            if arr_pointer[idx][0] != -1:
                arr_pointer[arr_pointer[idx][0]][1] = arr_pointer[idx][1]

            if arr_pointer[idx][1] != -1:
                arr_pointer[arr_pointer[idx][1]][0] = arr_pointer[idx][0]

            if arr_pointer[idx][2] != -1:
                arr_pointer[arr_pointer[idx][2]][3] = arr_pointer[idx][3]

            if arr_pointer[idx][3] != -1:
                arr_pointer[arr_pointer[idx][3]][2] = arr_pointer[idx][2]

            idx = arr_pointer[idx][0]

    elif  i == 'C':
        if arr_pointer[idx][1] != -1:

            if arr_pointer[idx][0] != -1:
                arr_pointer[arr_pointer[idx][0]][1] = arr_pointer[idx][1]

            if arr_pointer[idx][1] != -1:
                arr_pointer[arr_pointer[idx][1]][0] = arr_pointer[idx][0]

            if arr_pointer[idx][2] != -1:
                arr_pointer[arr_pointer[idx][2]][3] = arr_pointer[idx][3]

            if arr_pointer[idx][3] != -1:
                arr_pointer[arr_pointer[idx][3]][2] = arr_pointer[idx][2]

            idx = arr_pointer[idx][1]

    elif  i == 'A':
        if arr_pointer[idx][2] != -1:

            if arr_pointer[idx][0] != -1:
                arr_pointer[arr_pointer[idx][0]][1] = arr_pointer[idx][1]

            if arr_pointer[idx][1] != -1:
                arr_pointer[arr_pointer[idx][1]][0] = arr_pointer[idx][0]

            if arr_pointer[idx][2] != -1:
                arr_pointer[arr_pointer[idx][2]][3] = arr_pointer[idx][3]

            if arr_pointer[idx][3] != -1:
                arr_pointer[arr_pointer[idx][3]][2] = arr_pointer[idx][2]

            idx = arr_pointer[idx][2]

    elif  i == 'D':
        if arr_pointer[idx][3] != -1:

            if arr_pointer[idx][0] != -1:
                arr_pointer[arr_pointer[idx][0]][1] = arr_pointer[idx][1]

            if arr_pointer[idx][1] != -1:
                arr_pointer[arr_pointer[idx][1]][0] = arr_pointer[idx][0]

            if arr_pointer[idx][2] != -1:
                arr_pointer[arr_pointer[idx][2]][3] = arr_pointer[idx][3]

            if arr_pointer[idx][3] != -1:
                arr_pointer[arr_pointer[idx][3]][2] = arr_pointer[idx][2]

            idx = arr_pointer[idx][3]

print(*coord[idx])