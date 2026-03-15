import copy
N, M = map(int, input().split())
num_a = list(map(int, input().split()))
num_a.sort()
num_list = []
for i in num_a:
    num_list.append([i])


def NM1(N, M, num_list, list_a=None):
    #for initiate
    if list_a is None:
        list_a = copy.deepcopy(num_list)
        M -= 1
    for i in range(1, len(list_a)):
        if list_a[i] == list_a[i-1]:
            list_a[i-1] = -1
    list_a = [i for i in list_a if i != -1]
    
    if M == 0:
        return list_a

    next_list = []
    for list_b in list_a:
        for i in num_list:
            if i[0] >= list_b[-1]:
                next_list.append(list_b + i)

    for i in range(1, len(next_list)):
        if next_list[i] == next_list[i-1]:
            next_list[i-1] = -1
    next_list = [i for i in next_list if i != -1]

    return NM1(N, M-1, num_list, next_list)                

result = NM1(N, M, num_list)

for i in result:

    print(*i)