def moving(mains, up, right, down, left):

    if dir == '+':
        rotated = rights(mains)
        mains[:] = rotated
        temp = up[0][:]
        up[0] = left[0][:]
        left[0] = down[0][:]
        down[0] = right[0][:]
        right[0] = temp


    else:
        rotated = lefts(mains)
        mains[:] = rotated
        temp = up[0][:]
        up[0] = right[0][:]
        right[0] = down[0][:]
        down[0] = left[0][:]
        left[0] = temp

def rights(matrix):
    matrix2 = matrix[::-1]
    matrix3 = list(map(list, zip(*matrix2)))
    return matrix3

def lefts(matrix):
    matrix2 = list(map(list, zip(*matrix)))
    matrix3 = matrix2[::-1]
    return matrix3

def rotate180(matrix):
    return [row[::-1] for row in matrix[::-1]]


T = int(input())

for tc in range(1, T+1):
    t = int(input())
    orders = list(input().split())
    up_white = [['w'] * 3 for _ in range(3)]

    down_yellow = [['y'] * 3 for _ in range(3)]

    forward_red = [['r'] * 3 for _ in range(3)]

    back_orange = [['o'] * 3 for _ in range(3)]

    left_green = [['g'] * 3 for _ in range(3)]

    right_blue = [['b'] * 3 for _ in range(3)]

    for i in range(t):
        location = orders[i][0]
        dir = orders[i][1]

        if location == 'U':
            moving(up_white, back_orange, right_blue, forward_red, left_green)

        elif location == 'D':
            forward_red, right_blue, back_orange, left_green = rotate180(forward_red), rotate180(right_blue), rotate180(
                back_orange), rotate180(left_green)
            moving(down_yellow, forward_red, right_blue, back_orange, left_green)
            forward_red, right_blue, back_orange, left_green = rotate180(forward_red), rotate180(right_blue), rotate180(
                back_orange), rotate180(left_green)

        elif location == 'F':
            up_white, right_blue, down_yellow, left_green = rotate180(up_white), rights(right_blue), down_yellow, lefts(left_green)
            moving(forward_red, up_white, right_blue, down_yellow, left_green)
            up_white, right_blue, down_yellow, left_green = rotate180(up_white), lefts(right_blue), down_yellow, rights(left_green)

        elif location == 'R':
            up_white, back_orange, down_yellow, forward_red = lefts(up_white), rights(back_orange), lefts(down_yellow), lefts(forward_red)
            moving(right_blue, up_white, back_orange, down_yellow, forward_red)
            up_white, back_orange, down_yellow, forward_red = rights(up_white), lefts(back_orange), rights(down_yellow), rights(forward_red)

        elif location == 'B':
            up_white, left_green, down_yellow, right_blue = up_white, rights(left_green), rotate180(down_yellow), lefts(right_blue)
            moving(back_orange, up_white, left_green, down_yellow, right_blue)
            up_white, left_green, down_yellow, right_blue = up_white, lefts(left_green), rotate180(down_yellow), rights(right_blue)

        elif location == 'L':
            up_white, forward_red, down_yellow, back_orange = rights(up_white), rights(forward_red), rights(down_yellow), lefts(back_orange)
            moving(left_green, up_white, forward_red, down_yellow, back_orange)
            up_white, forward_red, down_yellow, back_orange = lefts(up_white), lefts(forward_red), lefts(down_yellow), rights(back_orange)

    for i in up_white:
        print(*i, sep='')