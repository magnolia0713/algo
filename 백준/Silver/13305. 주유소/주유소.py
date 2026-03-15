
n = int(input())

distance = list(map(int, input().split()))

price = list(map(int, input().split()))

min_price = price[0]

result = 0
for i in range(len(distance)):
    min_price = min(min_price, price[i])
    result += min_price * distance[i]

print(result)