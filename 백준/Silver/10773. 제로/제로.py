import sys
input = sys.stdin.readline
N = int(input())
a_list = [0] * N
top = -1
for i in range(N):
    num = int(input())
    if num == 0:
        a_list[top] = 0
        top -= 1
    else:
        top += 1
        a_list[top] = num
print(sum(a_list))