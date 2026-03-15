nums, n = map(int, input().split())
n_list = list(map(int, input().split()))

s = 1
e = max(n_list)

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for length in n_list:
        cnt += length // mid

    if cnt >= nums:
        s = mid + 1

    else:
        e = mid - 1

print(e)
