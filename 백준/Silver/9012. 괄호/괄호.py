N = int(input())
for _ in range(N):
    a_str = input()
    count = 0
    for i in range(len(a_str)):
        if a_str[i] == '(':
            count += 1
        else:
            count -= 1
            if count < 0 :
                print('NO')
                break

    else:
        if count == 0:
            print('YES')
        else:
            print('NO')