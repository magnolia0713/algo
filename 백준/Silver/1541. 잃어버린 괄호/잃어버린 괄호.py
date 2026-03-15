

num_list = list(input())

minus = False
number = []
total_cnt = 0

for i in num_list:
    if 48 <= ord(i) <= 57:
        number.append(i)

    else:
        temp_num = int(''.join(number))
        number.clear()

        if i == '+':
            if minus:
                total_cnt -= temp_num

            else:
                total_cnt += temp_num

        else:
            if minus:
                total_cnt -= temp_num

            else:
                total_cnt += temp_num

            minus = True

else:
    temp_num = int(''.join(number))
    number.clear()
    if minus:
        total_cnt -= temp_num

    else:
        total_cnt += temp_num


print(total_cnt)