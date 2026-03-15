a, b = input().split()

list_a = list(a)
list_b = list(b)

found = False
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            keep_a = i
            keep_b = j
            found = True
            break
    if found == True:
        break
                
matrix = list(list('.' * len(b)) for _ in range(len(a)))

matrix[keep_a] = list_b

matrix_org = list(map(list, zip(*matrix)))

matrix_org[keep_b] = list(a)


for i in range(len(b)):
    print(*matrix_org[i],sep = '')