scale = list(map(int,input().split()))

def discriminator(scale):
    list_dis = []
    for i in range(1,len(scale)):
        list_dis.append(scale[i] - scale[i-1])

    if list_dis.count(1) == len(list_dis):
        print('ascending')

    elif list_dis.count(-1) == len(list_dis):
        print('descending')

    else:
        print('mixed')


discriminator(scale)