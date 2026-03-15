

def func():
    info = {0}
    for i in range(n):
        info_add = set()
        for j in info:
            for k in range(1, coin_list[i][1] + 1):
                temp = j + coin_list[i][0] * k
                if temp == half:
                    return 1
                elif temp > half:
                    break
                else:
                    info_add.add(temp)

        info |= info_add

    else:
        return 0

for _ in range(3):
    n = int(input())
    coin_list = []
    total = 0
    for _ in range(n):
        coin_info = tuple(map(int, input().split()))
        total += coin_info[0] * coin_info[1]
        coin_list.append(coin_info)

    coin_list.sort(reverse=True)

    if total % 2 != 0:
        print(0)

    else:
        half = total // 2
        if coin_list[-1][0] == 1 and coin_list[-1][1] >= half:
            print(1)

        else:
            print(func())
