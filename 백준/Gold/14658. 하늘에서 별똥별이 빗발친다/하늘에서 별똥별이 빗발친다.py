n, m, r, num_of_star = map(int, input().split())

stars = []
for _ in range(num_of_star):
    stars.append(list(map(int, input().split())))

point = set()
for i in range(num_of_star):
    for j in range(i, num_of_star):
        point.add((min(stars[i][0],stars[j][0]),min(stars[i][1],stars[j][1])))

max_cnt = 0
for a, b in point:
    cnt = 0
    for p, q, in stars:
        if a <= p <= a + r and b <= q <= b + r:
            cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt

print(num_of_star - max_cnt)