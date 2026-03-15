T = int(input())

list_number = list(map(int, input().split()))

total_count = 0

def YIL(number):
    global total_count
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return    
    total_count += 1
        
            

for i in list_number:
    if i == 1:
        continue
    else:
        YIL(i)

print(total_count)