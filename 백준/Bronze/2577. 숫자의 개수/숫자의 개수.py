a = int(input())
b = int(input())
c = int(input())

number = str(a * b * c)

for i in range(10):
    used_number = number.count(str(i))
    print(used_number)