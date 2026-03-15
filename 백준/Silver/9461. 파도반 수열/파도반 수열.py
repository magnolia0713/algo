memo = [0] * 101
memo[1] = 1; memo[2] = 1; memo[3] = 1; memo[4] = 2; memo[5] = 2;


def recursion(n):

    if memo[n] == 0:
        memo[n] = recursion(n-1) + recursion(n-5)

    return memo[n]


t = int(input())

for _ in range(t):
    n = int(input())
    print(recursion(n))
