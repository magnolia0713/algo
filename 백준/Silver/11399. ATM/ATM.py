n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
cnt = 0

for idx in range(n):
    cnt += (n - idx) * n_list[idx]

print(cnt)