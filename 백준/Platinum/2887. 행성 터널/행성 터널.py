n = int(input())
n_list = []

def my_lord(p):
    if team[p] != p:
        team[p] = my_lord(team[p])

    return team[p]

def union(a, b):
    team[my_lord(b)] = team[my_lord(a)]

    return

for i in range(n):
    a, b, c = map(int, input().split())
    n_list.append((a,b,c,i))

a_list = sorted(n_list)
b_list = sorted(n_list, key=lambda x : x[1])
c_list = sorted(n_list, key=lambda x : x[2])
total_list = []

for i in range(n-1):
    total_list.append((abs(a_list[i+1][0] - a_list[i][0]), a_list[i][3], a_list[i+1][3]))
    total_list.append((abs(b_list[i+1][1] - b_list[i][1]), b_list[i][3], b_list[i+1][3]))
    total_list.append((abs(c_list[i+1][2] - c_list[i][2]), c_list[i][3], c_list[i+1][3]))
total_list.sort()

team = list(range(n))

cnt = 0
total_value = 0
for value, start, end in total_list:

    if my_lord(start) == my_lord(end):
        continue

    else:
        union(start, end)
        cnt += 1
        total_value += value
        if cnt == n-1:
            break

print(total_value)
