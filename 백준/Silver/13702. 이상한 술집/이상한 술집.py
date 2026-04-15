# 시간복잡도 1000 * 이분탐색 한 번
n, k = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

s = 1; e = max(n_list)

# 이분 탐색
a_max = 0
while s <= e:
    mid = (s + e) // 2
    total = 0
    for i in n_list:
        total += i // mid

    if total >= k:
        s = mid + 1
        if a_max < mid:
            a_max = mid
    else:
        e = mid - 1

print(a_max)