N, M = map(int, input().split())
num_list = sorted(map(int, input().split()))
check_list = [0] * N
list_a = []

def dfs():
    check = 0



    if len(list_a) == M:
        print(*list_a)
        return

    for i in range(len(num_list)):
        if check_list[i] == 0 and num_list[i] != check:
            if len(list_a) != 0:
                if list_a[-1] > num_list[i]:
                    continue
            check = num_list[i]
            list_a.append(num_list[i])
            check_list[i] = 1
            dfs()
            check_list[i] = 0
            list_a.pop()


dfs()