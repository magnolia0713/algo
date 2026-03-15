n = int(input())
memo = [0] * (n+1)
memo[0] = 1000001
memo[1] = 0

for i in range(2, n+1):
    if memo[i] == 0:
        memo[i] = min(memo[i//3] if i%3 == 0 else 1000000, memo[i//2] if i%2 == 0 else 1000000, memo[i-1]) + 1

print(memo[n])