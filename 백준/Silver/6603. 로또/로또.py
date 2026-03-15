def dfs(N, list_m, starting=0):
    
    if len(list_a) == 6:
        print(*list_a, sep=' ')
        return
        
    for i in range(starting, N):
        if checker[i] == 0:
            checker[i] = 1
            list_a.append(list_m[i])

            dfs(N, list_m, i+1)
            
            checker[i] = 0
            list_a.pop()

first_a = True

while True:
    if not first_a:
        print()
    first_a = False
    
    N, *M = map(int, input().split())
    if N == 0:
        break
    list_a = []
    list_m = list(M)
    
    checker = [0] * N
    dfs(N, list_m)