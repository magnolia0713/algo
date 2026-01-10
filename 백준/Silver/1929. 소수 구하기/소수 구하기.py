M, N = map(int,input().split())
num_arr = [True] * (N+1)
num_arr[0] = num_arr[1] = False

for i in range(2, M):
    if num_arr[i]:
        
        j = 1
        while i * j <= N:
            num_arr[i * j] = False
            j += 1

for i in range(M, N+1):
    if num_arr[i]:
        print(i)
        
        j = 1
        while i * j <= N:
            num_arr[i * j] = False
            j += 1
    