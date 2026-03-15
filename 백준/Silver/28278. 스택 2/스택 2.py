import sys
input = sys.stdin.readline
T = int(input())
a_list = []

for _ in range(T):
    t = list(map(int, input().split()))
    if t == [2]:
        if not a_list:
            print(-1)
        else:
            print(a_list.pop())
    
    elif t == [3]:
        print(len(a_list))
    
    elif t == [4]:
        if len(a_list) == 0:
            print(1)
        else:
            print(0)

    elif t == [5]:
        if not a_list:
            print(-1)
        else:
            print(a_list[-1])
            
    else:
        a_list.append(t[1])