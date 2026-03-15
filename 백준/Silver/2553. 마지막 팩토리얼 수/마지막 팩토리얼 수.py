N = int(input())
M = 1
for i in range(1,N+1):
    M *= i
    
a = list(str(M))
a.reverse()

for i in a:
    if i == '0':
        
        continue
    else:
        print(i)
        break
