
import sys
input = sys.stdin.readline

val = 1000000000
N = int(input())

#dp[자리수][끝자리 숫자][비트마스크]
dp = [[[0] * 1024 for _ in range(10)] for _ in range(N+1)]

# 초기값: 1자리 수는 1~9 (0으로 시작 X)
for i in range(1, 10):
    dp[1][i][1 << i] = 1

for length in range(2, N + 1):
    for num in range(10): 
        for bit in range(1024):
            if num > 0: # 0은 불가능
                dp[length][num][bit | (1 << num)] += dp[length - 1][num - 1][bit]
                dp[length][num][bit | (1 << num)] %= val
            if num < 9: # 9는 불가능
                dp[length][num][bit | (1 << num)] += dp[length - 1][num + 1][bit]
                dp[length][num][bit | (1 << num)] %= val

#(모든 숫자 사용) => 1023
answer = 0
for i in range(10):
    answer = (answer + dp[N][i][1023]) % val

print(answer)

