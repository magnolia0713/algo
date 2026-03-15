
def pibonacci(n):
    if n == 0:
        return memo[0]

    elif n == 1:
        return memo[1]

        
    if not memo[n]:
        memo[n] = (pibonacci(n-1)[0] + pibonacci(n-2)[0]), (pibonacci(n-1)[1] + pibonacci(n-2)[1])
    return memo[n]

        

test_case = int(input())


for _ in range(test_case):
    n = int(input())
    memo = [0] * (n+2)
    memo[0] = (1,0)
    memo[1] = (0,1)
    num_list = [0, 0]
    pibonacci(n)
    print(*memo[n])