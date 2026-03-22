
a, b, c = map(int, input().split())

d = int(input())

fixed_total = (a * 3600 + b * 60 + c + d) % 86400
h, temp = divmod(fixed_total, 3600)
m, s = divmod(temp, 60)
print(h, m, s)