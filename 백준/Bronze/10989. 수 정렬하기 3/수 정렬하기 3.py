import sys

def input():
    return sys.stdin.readline()



counter = [0] * 10001

N = int(input())

for _ in range(N):
    num = int(input())
    counter[num] += 1



for i in range(10001):
    if counter[i] != 0:
        for _ in range(counter[i]):
            print(i)
    