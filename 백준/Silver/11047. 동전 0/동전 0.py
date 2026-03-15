n, amount = map(int, input().split())

n_list = []

for _ in range(n):
    n_list.append(int(input()))

coin_cnt = 0
for coin in reversed(n_list):
    cnt, amount= divmod(amount, coin)
    coin_cnt += cnt

print(coin_cnt)
