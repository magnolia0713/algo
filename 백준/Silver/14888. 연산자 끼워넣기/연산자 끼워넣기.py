n = int(input())
n_list = list(map(int, input().split()))
calc_list = list(map(int, input().split()))
a_max = -1e11
a_min = 1e11

def dfs(depth, num):
    global a_max, a_min
    if depth == n-1:
        if a_max < num:
            a_max = num

        if a_min > num:
            a_min = num
        return

    for i in range(4):
        if calc_list[i]:

            calc_list[i] -= 1
            if i == 0:
                dfs(depth+1, num + n_list[depth+1])
            if i == 1:
                dfs(depth+1, num - n_list[depth+1])
            if i == 2:
                dfs(depth+1, num * n_list[depth+1])
            if i == 3:
                if num < 0:
                    dfs(depth + 1, -(-num // n_list[depth+1]))
                else:
                    dfs(depth + 1, num // n_list[depth+1])

            calc_list[i] += 1

dfs(0, n_list[0])

print(a_max)
print(a_min)