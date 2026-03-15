n = list(input())
cnt = 0

i = 1
pointer = 0
while pointer < len(n):
    p = str(i)
    
    flag = False
    for j in range(len(p)):
        if pointer < len(n):
            if n[pointer] == p[j]:
                flag = True
                pointer += 1
    i += 1

print(i - 1)