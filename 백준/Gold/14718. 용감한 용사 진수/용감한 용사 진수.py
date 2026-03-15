
m, n = map(int, input().split())
a_list = []
bc_list = []
org_list = []
for i in range(m):
    a,b,c = map(int, input().split())
    org_list.append((a,b,c))
    a_list.append(a)
    bc_list.append((b,c))


tuple_list = []
for i in a_list:
    for j,k in bc_list:
        tuple_list.append((i,j,k))

total_list = sorted(tuple_list)
k_list = sorted(org_list,key=lambda x:x[2])

final_list = []
for r, c, _ in total_list:
    temp = []
    for p, q, t in k_list:
        if r >= p and c >= q:
            temp.append((r,c,t))
    if len(temp) >= n:
        final_list.append(temp[n-1])

min_sum = 1000000000
for i in final_list:
    if min_sum > sum(i):
        min_sum = sum(i)

print(min_sum)