N = int(input())

list_a = []
for profile in range(N):
    age, name = input().split()
    list_a.append((int(age), profile, name))

list_a.sort(key = lambda x : (x[0],x[1]))

for i in list_a:
    print(f"{i[0]} {i[2]}")