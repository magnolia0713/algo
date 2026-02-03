a, b = input().split()

diff = len(b) - len(a)
a_max = 0
for i in range(diff+1):
    cnt = 0

    for j in range(len(a)):
        if a[j] == b[j+i]:
            cnt += 1

    if a_max < cnt:
        a_max = cnt

print(len(a) - a_max)

