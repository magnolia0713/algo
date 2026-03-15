n, t = map(int, input().split())
n_list = []
n_list.append(int(input()))
sorted_list = []
for i in range(1, n):
    n_list.append(int(input()))
    sorted_list.append(n_list[i] - n_list[i-1])

sorted_list.sort()
temp = n - t
print(sum(sorted_list[:temp]) + t)