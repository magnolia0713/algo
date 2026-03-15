list_a = list(map(int, list(input())))
list_b = list(map(int, list(input())))
list_c = list(map(int, list(input())))
list_d = list(map(int, list(input())))
N = int(input())
top_a = top_b = top_c = top_d = 0
for _ in range(N):
    i, j = map(int, input().split())

    if j == -1:
        if i == 1 or i == 3:
            dirs = [1, -1, 1, -1]
        else:
            dirs = [-1, 1, -1, 1]

    else:
        if i == 1 or i == 3:
            dirs = [-1, 1, -1, 1]
        else:
            dirs = [1, -1, 1, -1]

    if i == 1:
        if list_a[(top_a+2)%8] == list_b[(top_b+6)%8]:
            top_a = (top_a + dirs[0]) % 8
        else:
            top_a = (top_a + dirs[0]) % 8

            if list_b[(top_b+2)%8] == list_c[(top_c+6)%8]:
                top_b = (top_b + dirs[1]) % 8
            else:
                top_b = (top_b + dirs[1]) % 8

                if list_c[(top_c+2)%8] == list_d[(top_d+6)%8]:
                    top_c = (top_c + dirs[2]) % 8

                else:
                    top_c = (top_c + dirs[2]) % 8
                    top_d = (top_d + dirs[3]) % 8

    elif i == 2:
        if list_b[(top_b+6)%8] == list_a[(top_a+2)%8]:
            pass
        else:
            top_a = (top_a + dirs[0]) % 8

        if list_b[(top_b + 2) % 8] == list_c[(top_c + 6) % 8]:
            top_b = (top_b + dirs[1]) % 8
        else:
            top_b = (top_b + dirs[1]) % 8

            if list_c[(top_c + 2) % 8] == list_d[(top_d + 6) % 8]:
                top_c = (top_c + dirs[2]) % 8

            else:
                top_c = (top_c + dirs[2]) % 8
                top_d = (top_d + dirs[3]) % 8

    elif i == 3:
        if list_b[(top_b + 2) % 8] == list_c[(top_c + 6) % 8]:
            pass
        else:
            pass

            if list_a[(top_a + 2) % 8] == list_b[(top_b + 6) % 8]:
                top_b = (top_b + dirs[1]) % 8
            else:
                top_a = (top_a + dirs[0]) % 8
                top_b = (top_b + dirs[1]) % 8

        if list_c[(top_c + 2) % 8] == list_d[(top_d + 6) % 8]:
            top_c = (top_c + dirs[2]) % 8

        else:
            top_c = (top_c + dirs[2]) % 8
            top_d = (top_d + dirs[3]) % 8



    elif i == 4:
        if list_c[(top_c + 2) % 8] == list_d[(top_d + 6) % 8]:
            top_d = (top_d + dirs[3]) % 8
        else:
            top_d = (top_d + dirs[3]) % 8

            if list_b[(top_b + 2) % 8] == list_c[(top_c + 6) % 8]:
                top_c = (top_c + dirs[2]) % 8
            else:
                top_c = (top_c + dirs[2]) % 8

                if list_a[(top_a + 2) % 8] == list_b[(top_b + 6) % 8]:
                    top_b = (top_b + dirs[1]) % 8
                else:
                    top_a = (top_a + dirs[0]) % 8
                    top_b = (top_b + dirs[1]) % 8

print(list_a[top_a] + list_b[top_b]*2 + list_c[top_c]*4 + list_d[top_d]*8)

