n = int(input())
n_list = list(map(int, input().split()))
grow_list = list(map(int, input().split()))
adjusted_list = []
for i in range(n):
    adjusted_list.append((grow_list[i],i))

adjusted_list.sort()

cnt = 0
for i in range(n):
    cnt += adjusted_list[i][0] * i + n_list[adjusted_list[i][1]]

print(cnt)