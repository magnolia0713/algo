
n = int(input())

plus_arr = []
one_arr = []
minus_arr = [] # 0이 이 곳에 들어가야 편해질 것 같다.

for i in range(n):
    n = int(input())
    if n > 1:
        plus_arr.append(n)

    elif n == 1:
        one_arr.append(1)
    else:
        minus_arr.append(n)


plus_arr.sort(reverse=True); minus_arr.sort()

total = len(one_arr)

if len(plus_arr) % 2 != 0:
    total += plus_arr.pop()

if len(minus_arr) % 2 != 0:
    total += minus_arr.pop()

for i in range(0, len(plus_arr), 2):
    total += plus_arr[i] * plus_arr[i + 1]

for i in range(0, len(minus_arr), 2):
    total += minus_arr[i] * minus_arr[i + 1]


print(total)