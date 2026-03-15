min_a = int(input())
max_a = int(input())

if min_a == 1:
    min_a += 1

list_prime = []

for i in range(min_a,max_a+1):
    list_div = []

    for j in range(2,int(i ** 0.5) + 1):
        if i % j == 0:
            list_div.append(j)
    
    if len(list_div) == 0:
        list_prime.append(i)


if len(list_prime) == 0:
    print(-1)


else:
    print(sum(list_prime))
    print(min(list_prime))