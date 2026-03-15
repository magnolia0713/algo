number = int(input())

while number != -1:
    list_divisor = []
    for i in range (1, int(number/2 + 1)):
        if number % i == 0:
            list_divisor.append(i)
    
    
    if sum(list_divisor) == number:
        list_div_str = list(map(str, list_divisor))
        print(f"{number} = {' + '.join(list_div_str)}")

    else:
        print(f"{number} is NOT perfect.")

    number = int(input())