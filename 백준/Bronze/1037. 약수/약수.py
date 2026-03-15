T = int(input())

list_a = list(map(int, input().split()))

list_a.sort()

number_a = list_a[0] * list_a[-1]

print(number_a)