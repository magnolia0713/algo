len_x, len_y = map(int, input().split())

T = int(input())

for_x = [0,len_x]
for_y = [0,len_y]
    
for t in range(T):
    direction, number = map(int,input().split())
    
    if direction == 1:
        for_x.append(number)
    
    else:
        for_y.append(number)
    
for_x.sort()
for_y.sort()
max_x = 0
max_y = 0

for index in range(1, len(for_x)):
    if for_x[index] - for_x[index-1] > max_x:
        max_x = for_x[index] - for_x[index-1]
        

    
for index in range(1, len(for_y)):
    if for_y[index] - for_y[index-1] > max_y:
        max_y = for_y[index] - for_y[index-1]
        
print(max_x * max_y)