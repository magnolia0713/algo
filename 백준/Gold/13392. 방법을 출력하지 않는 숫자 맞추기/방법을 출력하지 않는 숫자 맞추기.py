n = int(input())

a = input()
b = input()
diff = []

# 이제까지 돌려진 횟수를 기록 각 2번째 dp에는 회전이 일어난 횟수(0~9)
dp = [[111111] * 10 for _ in range(n)]
for i in range(n):

    diff.append((ord(b[i]) - ord(a[i]) + 10) % 10)

#print(diff)

# 다른 변수는 입력 불가능을 위한

dp[0][diff[0]] = diff[0]
dp[0][0] = (10 - diff[0]) % 10
#print(dp[0])
for idx in range(1, n):
    for i in range(10):
        # 밑에 영향을 주는 회전
        temp = (diff[idx] - i + 10) % 10
        dp[idx][(i + temp) % 10] = min(dp[idx][(i + temp) % 10], dp[idx-1][i] + temp)
        #영향을 주지 않는 회전
        dp[idx][i] = min(dp[idx][i], dp[idx-1][i] + (10 - temp) % 10)

# for i in dp:
#     print(i)
print(min(dp[-1]))


