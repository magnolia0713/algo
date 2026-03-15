def recursion(n):
    if n == 1:
        return('- -')

    result = recursion(n-1) + (' '*(3**(n-1))) + recursion(n-1)
    return result

while True:
    try:
        n = int(input())

    except:
        break

    if n == 0:
        print('-')

    else:
        print(recursion(n))