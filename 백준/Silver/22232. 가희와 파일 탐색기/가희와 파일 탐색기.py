import sys
input = sys.stdin.readline

N, M = map(int, input().split())

files = []
for _ in range(N):
    s = input().strip()
    name, ext = s.rsplit('.', 1)
    files.append((name, ext))

known = set()
for _ in range(M):
    known.add(input().strip())

files.sort(key=lambda x: (x[0], 0 if x[1] in known else 1, x[1]))

for name, ext in files:
    print(name + '.' + ext)