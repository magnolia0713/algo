n = int(input())

n_list = []

for _ in range(n):
    n_list.append(tuple(map(int, input().split())))

n_list.sort(key=lambda x: (x[1],x[0]))

end = -1
cnt = 0
for i, j in n_list:

    if end <= i:
        cnt += 1
        end = j

print(cnt)