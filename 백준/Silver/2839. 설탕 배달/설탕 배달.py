N = int(input())

bag_3 = N // 3

check = False

for i in range(bag_3 + 1):
    for j in range(N//5 + 1):
        if N - 3 * i - 5 * j == 0:
            print(i+j)
            check = True
            break
    if check == True:
        break
else:
    print(-1)