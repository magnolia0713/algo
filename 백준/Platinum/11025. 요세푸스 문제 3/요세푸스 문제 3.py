n, k = map(int, input().split())

j = 0
for i in range(1, n + 1):
    j = (j + k) % i

print(j + 1) 