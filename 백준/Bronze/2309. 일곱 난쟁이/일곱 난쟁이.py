a_list = []
for _ in range(9):
    a_list.append(int(input()))
sum_list = []
checker = [0] * 9

def finder():
    
    if len(sum_list) == 7:
        if sum(sum_list) == 100:
            sum_list.sort()
            print(*sum_list, sep='\n')

            return True

    else:
        
        for i in range(9):
            if checker[i] == 0:
                sum_list.append(a_list[i])
                checker[i] = 1
                if finder():
                    return True
                sum_list.pop()
                checker[i] = 0

finder()