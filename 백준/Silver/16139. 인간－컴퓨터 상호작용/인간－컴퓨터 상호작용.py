import sys
input = sys.stdin.readline

S = input().strip()
n = len(S)

# prefix[i][c] : S[0..i-1]까지 c 개수 (i는 0..n)
prefix = [[0] * 26 for _ in range(n + 1)]

for i, ch in enumerate(S):
    # 이전 값 복사
    prefix[i + 1] = prefix[i][:]
    prefix[i + 1][ord(ch) - 97] += 1

q = int(input().strip())
out = []
for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    idx = ord(a) - 97
    out.append(str(prefix[r + 1][idx] - prefix[l][idx]))

print("\n".join(out))
