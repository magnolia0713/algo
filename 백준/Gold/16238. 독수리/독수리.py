
n = int(input())
memo = [[0] * (n) for _ in range(n)]
pray = list(map(int, input().split()))
memo[0][0] = pray[0]

def not_minus(num, value):
    if num - value > 0:
        return num - value
    else:
        return 0

for r in range(1, n):
    memo[0][r] = max(pray[r], memo[0][r-1])
    memo[r][r] = memo[r-1][r-1] + not_minus(pray[r], r)


for r in range(1,n):
    for c in range(r+1, n):
        memo[r][c] = max(memo[r][c-1], (memo[r-1][c-1] + not_minus(pray[c], r)))

# for i in memo:
#     print(*i)

a_max = 0
for r in range(n):
    for c in range(r, n):
        if a_max < memo[r][c]:
            a_max = memo[r][c]

print(a_max)