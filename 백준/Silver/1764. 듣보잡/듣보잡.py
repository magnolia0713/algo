import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heard = []
pointer = 0
heard_seen = []
for _ in range(n+m):
    word = input().strip()
    heard.append(word)
heard.sort()

for i in range(n+m-1):
    if heard[i] == heard[i+1]:
        heard_seen.append(heard[i])
print(len(heard_seen))
print(*heard_seen, sep='\n')

