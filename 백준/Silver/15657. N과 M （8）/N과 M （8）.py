N, M = map(int, input().split())
num_a = list(map(int, input().split()))
num_a.sort()
num_list = []
for i in num_a:
    num_list.append([i])

def NM1(N, M, num_list, list_a=None):
    #for initiate
    if list_a is None:
        list_a = num_list
        M -= 1

    if M == 0:
        return list_a

    next_list = []
    for list_b in list_a:
        for i in num_list:
            if i[0] >= list_b[-1]:
                next_list.append(list_b + i)
    return NM1(N, M-1, num_list, next_list)                

result = NM1(N, M, num_list)
for i in result:
    print(*i)