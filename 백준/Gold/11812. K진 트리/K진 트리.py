import sys
input = sys.stdin.readline
def location(num):

    i = 0
    while True:
        if num - (K ** i) < 0:
            result = []
            for _ in range(i + 1):
                result.append(num % K)
                num //= K
            break
        else:
            num -= (K ** i)
            i += 1
    result.reverse()

    return result


N, K, Q = map(int, input().split())

if K == 1:
    for _ in range(Q):
        a, b = map(int, input().split())
        print(abs(a-b))

else:
    for _ in range(Q):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        line_a = location(a)
        line_b = location(b)


        for i in range(min(len(line_a),len(line_b))):
            if line_a[i] != line_b[i]:
                print(len(line_a) + len(line_b) - 2*i)
                break

        else:
            print(len(line_a) + len(line_b) - 2 * i - 2)