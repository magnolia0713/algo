n = int(input())
a_arr = list(map(int, input().split()))

a_sum = 0
a_max = -2100
for i in range(n):
    a_sum += a_arr[i]

    if a_max < a_sum:
        a_max = a_sum

    if a_sum < 0:
        a_sum = 0

print(a_max)