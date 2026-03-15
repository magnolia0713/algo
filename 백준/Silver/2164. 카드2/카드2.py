
n = int(input())

n_list = list(range(1,n+1))

head = 0
tail = n - 1
turns = 0
while head != tail:
    if turns:
        n_list.append(n_list[head])
        head += 1
        tail += 1
        

    else:
        head += 1    

    turns = 1 - turns

print(n_list[head])
    
