import sys
input = sys.stdin.readline

S = set()
n = int(input())

for _ in range(n):
    received = input().split()
    
    if len(received) == 1:
        cmd = received[0]
        if cmd == 'all':
            S = set(range(1, 21))
        else:  # 'empty'
            S.clear()
    else:
        cmd, x = received[0], int(received[1])
        
        if cmd == 'add':
            S.add(x)
        elif cmd == 'remove':
            S.discard(x)  # safer than remove
        elif cmd == 'check':
            print(1 if x in S else 0)
        elif cmd == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)
