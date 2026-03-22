import sys
input = sys.stdin.readline
test_case = int(input())
# 숫자가 끝나는 곳에 가능한지 안한지만 탐색한다면 ?
dp = [[0] * 10 for _ in range(65)]
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 0행은 항상 1
for i in range(2, 65):
    dp[i][0] = 1

# 열을 채우자.
for i in range(2, 65):
    for j in range(1, 10):
        dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

counter = [0] * 65
for i in range(1,65):
    counter[i] = sum(dp[i])

for _ in range(test_case):
    print(counter[int(input())])