def dfs(starting, depth=0):
    
    if depth == L:
        if list_word.count('a') + list_word.count('e') + list_word.count('i') + list_word.count('o') + list_word.count('u')>= 1 and list_word.count('a') + list_word.count('e') + list_word.count('i') + list_word.count('o') + list_word.count('u') < L - 1: 
            print(*list_word, sep = '')
        return
    
    for i in range(starting, C):
        if check_a[i] == 0:
            list_word.append(list_a[i])
            check_a[i] = 1

            dfs(i+1, depth+1)

            check_a[i] = 0
            list_word.pop()

    return

L, C = map(int, input().split())

list_a = list(input().split(' '))
check_a = [0] * C

list_a.sort()
list_word = []

dfs(0)

