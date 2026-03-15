room_number = int(input())

for i in range(0,100000):
    if room_number <= 6 * i + 1:
        print(i+1) 
        break
    else:
        room_number -= 6 * i