n = int(input())

n_list = list(map(int, input().split()))
n_list.sort()


# 홀수, 짝수 일 때 분리
# a를 짝수로 하자.
a_min = 1e10
b_min = 1e10

for i in range(1, len(n_list)):
    temp = n_list[i] - n_list[i-1]
    if temp % 2:
        if b_min > temp:
            b_min = temp
        if i > 1 and (n_list[i] - n_list[i-2]) % 2 == 0 and a_min > n_list[i] - n_list[i-2]:
            a_min = n_list[i] - n_list[i - 2]

    else:
        if a_min > temp:
            a_min = temp

if a_min > 2e9:
    a_min = -1
if b_min > 2e9:
    b_min = -1

print(a_min, b_min)

