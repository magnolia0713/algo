n = int(input())
n_list = list(map(int, input().split()))

# 비감소로 만들기
drops = 0
inc = 0

# 비증가로 만들기
rises = 0
dec = 0

for i in range(n - 1):
    if n_list[i] > n_list[i + 1]:
        drops += 1
        inc = i + 1
    elif n_list[i] < n_list[i + 1]:
        rises += 1
        dec = i + 1
    # 같으면 아무것도 안 함

cands = []

# 비감소 후보
if drops == 0:
    cands.append(0)
elif drops == 1 and n_list[-1] <= n_list[0]:
    cands.append(inc)

# 비증가 후보
if rises == 0:
    cands.append(0)
elif rises == 1 and n_list[-1] >= n_list[0]:
    cands.append(dec)

print(min(cands) if cands else -1)