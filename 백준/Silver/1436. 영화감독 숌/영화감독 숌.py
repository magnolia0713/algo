N = int(input())

number = 665
count = 0

while count != N:
    if '666' in str(number):    
        count += 1
        last_number = number
    number += 1


print(last_number)