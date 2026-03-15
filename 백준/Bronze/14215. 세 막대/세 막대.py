list_length = list(map(int, input().split()))

list_length.sort()

if list_length[0] + list_length[1] > list_length[2]:
    print(sum(list_length))

else:
    print((list_length[0] + list_length[1]) * 2 - 1)