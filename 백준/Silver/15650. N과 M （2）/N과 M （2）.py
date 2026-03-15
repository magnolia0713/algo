import copy
N, M = map(int, input().split())

list_a = []
list_b = []

def NM1(N, M):
    
    global list_a
    global list_b
    if list_a == []:
        list_a = [[i] for i in range(1,N+1)]
        M -= 1

    if M == 0:
        return
    else:
        for num in list_a:
            for i in range(1, N+1):
                if i not in num:
                    num_1 = num + [i]
                    list_b.append(num_1)
        list_a = copy.deepcopy(list_b)
        list_b.clear()

        return NM1(N, M-1)

NM1(N, M)

for list_a in list_a:
    for i in range(1, len(list_a)):
        if list_a[i] <= list_a[i-1]:
            break
    else:
        print(*list_a)