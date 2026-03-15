
def func():
    count = 0
    stack = ''
    for i in word_arr:
        if i == 'X':
            count += 1

        else:
            if not count % 2:
                if count % 4:
                    stack += 'AAAA' * (count // 4)
                    stack += 'BB'

                else:
                    stack += 'AAAA' * (count // 4)

            else:
                return -1

            stack += '.'
            count = 0

    else:
        if not count % 2:
            if count % 4:
                stack += 'AAAA' * (count // 4)
                stack += 'BB'

            else:
                stack += 'AAAA' * (count // 4)
        else:
            return -1

    return stack

word_arr = list(input())
print(func())