T = int(input())

for t in range(T):

    N, M = map(int,input().split())
    
    total_number = 1

    for i in range(M, M-N,-1):
        total_number *= i
        total_number /= M-i + 1

    print(int(total_number))