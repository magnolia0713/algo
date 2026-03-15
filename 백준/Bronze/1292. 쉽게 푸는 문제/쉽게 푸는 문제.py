A, B = map(int,input().split())

list_A = []

for i in range(1, 47):
    list_A += [i] * i


print(sum(list_A[A-1:B]))