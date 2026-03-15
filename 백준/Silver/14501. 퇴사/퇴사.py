def dfs(day, pay):
    if day > N:
        a_sum.add(pay)
        return

    for a_limit in range(day-1, len(a_list)):
        if a_list[a_limit][0] + a_list[a_limit][1] > N+1:
            a_sum.add(pay)

        else:
            dfs(a_list[a_limit][0] + a_list[a_limit][1],pay + a_list[a_limit][2])


#-------------------------
N = int(input())
a_list = []
for i in range(1, N+1):
    t, p = map(int, input().split())
    a_list.append([i, t, p])

a_sum = {0}

dfs(1, 0)
print(max(a_sum))