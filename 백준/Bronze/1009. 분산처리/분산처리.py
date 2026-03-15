import sys
t = int(sys.stdin.readline())

cycles = {
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10
    cycle = cycles[a]
    idx = (b - 1) % len(cycle)
    result = cycle[idx]
    print(10 if result == 0 else result)