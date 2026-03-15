N, M = map(int, input().split())



def NM1(N, M, list_a=None):
    #for initiate
    if list_a is None:
        list_a = [[i] for i in range(1, N+1)]
        M -= 1

    if M == 0:
        return list_a

    next_list = []
    for list_b in list_a:
        for i in range(1, N+1):
            next_list.append(list_b + [i])
    return NM1(N, M-1, next_list)                

result = NM1(N, M)
for i in result:
    print(*i)