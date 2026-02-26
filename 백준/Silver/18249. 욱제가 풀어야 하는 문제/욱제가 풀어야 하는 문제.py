import sys
input = sys.stdin.readline
test_case = int(input())
dp = [0] * 200000
dp[0] = 0
dp[1] = 1
dp[2] = 2
for i in range(3, 191230):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

for _ in range(test_case):
    print(dp[int(input())])

