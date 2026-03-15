switch = int(input())

list_bulb = list(map(int, input().split()))

stu_num = int(input())
list_gen_num = list(tuple(map(int, input().split())) for _ in range(stu_num))

def male_func(swit_num, list_bulb):
    k = swit_num
    while True:
        
        try:
            if list_bulb[swit_num-1] == 0:
                list_bulb[swit_num-1] = 1
            else:
                list_bulb[swit_num-1] = 0
            swit_num += k
        
        except:
            return list_bulb

def female_func(swit_num, list_bulb):
    
    swit_num -= 1
    if list_bulb[swit_num] == 1:
         list_bulb[swit_num] = 0
    
    else:
        list_bulb[swit_num] = 1
    n = 1  

    while True:
        if swit_num - n < 0 or swit_num + n > switch - 1:
            return list_bulb
            
        elif list_bulb[swit_num - n] == list_bulb[swit_num + n]:
        
            if list_bulb[swit_num - n] == 0:
                list_bulb[swit_num - n] = 1
                list_bulb[swit_num + n] = 1
            else:
                list_bulb[swit_num - n] = 0
                list_bulb[swit_num + n] = 0
                
            n += 1
        else:
            return list_bulb
        
            
            
            
        
for gender, swit_num in list_gen_num:
    if gender == 1:
        list_bulb = male_func(swit_num, list_bulb)
    else:
        list_bulb = female_func(swit_num, list_bulb)
        
        

for i in range(1, len(list_bulb)+1):
    print(list_bulb[i-1], end = ' ')
    
    if i % 20 == 0:
        if i != len(list_bulb)+1:
            print()