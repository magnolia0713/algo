N = int(input())
a_list = list(map(int, input().split()))
M = int(input())
b_list = list(map(int, input().split()))

a_dict = {}
for i in a_list:
    if i in a_dict:
        a_dict[i] += 1
    else:
        a_dict[i] = 1

ans_list = []

for j in b_list:
    if j in a_dict:
        ans_list.append(a_dict[j])
    else:
        ans_list.append(0)

print(*ans_list)