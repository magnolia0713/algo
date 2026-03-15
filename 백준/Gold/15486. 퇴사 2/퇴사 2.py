import sys
input = sys.stdin.readline
N = int(input())
a_list = [[]]
memo = [0] * (N+51)
for day in range(1,N+1):
    i, j = list(map(int, input().split()))
    if memo[day-1] + j > memo[day + i - 1]:
        memo[day + i - 1] = memo[day-1] + j
    if memo[day] < memo[day-1]:
        memo[day] = memo[day-1]
print(memo[N])