room_number = int(input())

for i in range(1,10000):
    if room_number <= i:
        if i % 2 == 1:
            print(f"{i-room_number+1}/{room_number}")
        
        else:
            print(f"{room_number}/{i-room_number+1}")
        break
    else:
        room_number -= i