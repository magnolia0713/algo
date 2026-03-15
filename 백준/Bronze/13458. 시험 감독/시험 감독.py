N = int(input())
a_list = list(map(int, input().split()))
n, m = map(int, input().split())
count = 0
for i in a_list:
    if n >= i:
        count += 1
        continue
    else:
        count += (i-n-1) // m + 2

print(count)