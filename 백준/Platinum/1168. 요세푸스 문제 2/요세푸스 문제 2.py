
#import time


#starts = time.time()
n, k = map(int, input().split())
if n == k == 1:
    print("<1>")

else:
    # 트리를 만들기 위한 인덱스 설치
    m = n - 1
    depth = 0
    while m:
        depth += 1
        m //= 2

    depth_width = 2**depth
    tree = [0] * (depth_width + n)

    #출력 배열은 여기에 저장
    for i in range(depth_width, depth_width + n):
        tree[i] = 1
        while i:
            i //= 2
            tree[i] += 1


    # 순서 출력
    ans_arr = []

    idx = 0
    for i in range(n):
        idx += k - 1
        tree_idx = 1
        idx %= tree[tree_idx]
        temp = idx
        tree[tree_idx] -= 1
        tree_idx += 1

        while True:
            if tree_idx >= depth_width:
                if not temp and tree[tree_idx] == 1:
                    tree[tree_idx] -= 1
                    ans_arr.append(tree_idx - depth_width + 1)

                else:
                    tree[tree_idx+1] -= 1
                    ans_arr.append(tree_idx - depth_width + 2)
                break

            elif tree[tree_idx] > temp:
                tree[tree_idx] -= 1
                tree_idx *= 2

            else:
                temp -= tree[tree_idx]
                tree[tree_idx+1] -= 1
                tree_idx = (tree_idx+1) * 2

    print(f"<", end='')
    for i in range(len(ans_arr)-1):
        print(ans_arr[i], end=', ')

    print(f"{ans_arr[-1]}>")
#ends = time.time()

#print(ends - starts)
