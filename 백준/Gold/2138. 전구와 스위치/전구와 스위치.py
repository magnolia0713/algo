

n = int(input())

a_arr = list(map(int, input()))
b_arr = list(map(int, input()))

c_arr = [0] * (n+1)

for i in range(n):
    c_arr[i] = abs(a_arr[i] - b_arr[i])

d_arr = c_arr.copy()

d_arr[0] = (1 - c_arr[0]) ; d_arr[1] = (1 - c_arr[1])

c_cnt = 0
d_cnt = 1

for i in range(n-1):
    if c_arr[i]:
        c_arr[i] = (1-c_arr[i])
        c_arr[i+1] = (1-c_arr[i+1])
        c_arr[i+2] = (1-c_arr[i+2])
        c_cnt += 1

if d_arr[0]:
    for i in range(n-1):
        if d_arr[i]:
            d_arr[i] = (1-d_arr[i])
            d_arr[i+1] = (1-d_arr[i+1])
            d_arr[i+2] = (1-d_arr[i+2])
            d_cnt += 1

else:
    d_arr[-2] = 1

if c_arr[-2] and d_arr[-2]:
    print(-1)

elif not c_arr[-2]:
    print(c_cnt)

else:
    print(d_cnt)