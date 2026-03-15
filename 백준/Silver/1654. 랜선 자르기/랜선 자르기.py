n, m = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

s = 1; e = max(n_list)

while s <= e:

    mid = (s + e) // 2
    cnt = 0
    for i in n_list:
        cnt += i // mid

    if cnt >= m:
        s = mid + 1

    else:
        e = mid - 1

print(e)