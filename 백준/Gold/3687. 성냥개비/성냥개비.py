import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    a = (n // 2)

    if n % 2 == 1:

        a_max = int('7' +'1' * (a - 1))

    else:
        a_max = int('1' * a)

    b = n // 7
    remains = (7 - n % 7) if n % 7 != 0 else 0
    a_min = ''
    if remains:
        b += 1



    while b > 1:

        if not remains:
            a_min += '8' * b
            break

        elif a_min:
            a_min += '0'
            remains -= 1
            b -= 1

        elif remains == 1:

            a_min += '6'
            remains = 0
            b -= 1

        #앞에 수가 없을 경우에
        elif remains >= 5:
            a_min += '1'
            remains -= 5
            b -= 1


        elif remains >= 2:
            a_min += '2'
            remains -= 2
            b -= 1

    if b == 1 and not remains:
        a_min += '8'

    if remains:
        if remains == 5:
            a_min += '1'

        elif remains == 4:
            a_min += '7'

        elif remains == 3:
            a_min += '4'

        elif remains == 2:
            a_min += '2'

        elif remains == 1:
            if a_min:
                a_min += '0'
            else:
                a_min = 6



    print(a_min, a_max)

    b = (n // 7)
