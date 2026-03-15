N, M = map(int, input().split())
num_list = list(range(1,N+1))
check_list = [0] * N
list_a = []

def dfs():
    if len(list_a) == M:
        print(*list_a)
        return

    for i in range(len(num_list)):
        if check_list[i] == 0:
            list_a.append(num_list[i])
            check_list[i] = 1
            dfs()
            check_list[i] = 0
            list_a.pop()

dfs()