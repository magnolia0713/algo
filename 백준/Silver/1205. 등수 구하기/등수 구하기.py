
n, score, cut = map(int, input().split())

if n == 0:
    print(1)

else:
    a_list = list(map(int, input().split()))


    a_list.sort(reverse=True)
    def grade():
        cnt = 1
        mini_cnt = 0
        for i in range(n):
            if a_list[i] > score:
               cnt += 1

            elif a_list[i] == score:
                mini_cnt += 1

            else:
                if cnt + mini_cnt > cut:
                    return -1

                break
        else:
            if cnt + mini_cnt > cut:
                return -1

        return cnt


    print(grade())

