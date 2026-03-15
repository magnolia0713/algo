T = int(input())

cont_set = {'ChongChong'}

for _ in range(T):
    a, b = input().split()
    if a in cont_set or b in cont_set:
        cont_set.add(a)
        cont_set.add(b)


number_cont = len(cont_set)


print(number_cont)