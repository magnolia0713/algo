import sys
input = sys.stdin.readline

n = int(input())
n_list = []
a_list = []
b_list = []
for _ in range(n):
    n_list.append(tuple(map(int, input().split())))

for i in range(n):
    for j in range(n):
        a_list.append(n_list[i][0] + n_list[j][1])
        b_list.append(n_list[i][2] + n_list[j][3])

a_list.sort()
b_list.sort()
head = 0
tail = len(b_list) - 1
cnt = 0

while head < len(a_list) and tail >= 0:

    if a_list[head] + b_list[tail] > 0:
        tail -= 1

    elif a_list[head] + b_list[tail] < 0:
        head += 1

    else:
        a = 1
        b = 1
        while True:
            if head + a < len(a_list) and a_list[head] == a_list[head + a]:
                a += 1
            else:
                break

        while True:
            if tail - b >= 0 and b_list[tail] == b_list[tail - b]:
                b += 1

            else:
                break

        cnt += a * b
        head += a
        tail -= b

print(cnt)
