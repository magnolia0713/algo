from sys import stdin

input = stdin.readline

# 좌표압축을 동시에 진행하자.
x_list = []
y_list = []
n = int(input())
n_list = []
ordered_list = []

for _ in range(n):
    x, y, w = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    n_list.append((x, y, w))

# 좌표압축용 배열 정렬
x_list.sort(); y_list.sort()
x_set = {}; y_set = {}

# 중복이면 뒤의 값이 저장이 되겠지? 아마.
for i in range(n):
    x_set[x_list[i]] = i
    y_set[y_list[i]] = i

for x, y, w in n_list:
    ordered_list.append((x_set[x], y_set[y], w))

ordered_list.sort(key=lambda x:x[1])
#print(ordered_list)

# n값에 맞는 seg_tree를 만들어보자.
added_length = 2 ** ((n-1).bit_length())

max_advantage = 0
# 같은 y끼리 묶인 구간의 시작/끝 인덱스 만들기
row_ranges = []
s = 0
while s < n:
    e = s
    cur_y = ordered_list[s][1]
    while e < n and ordered_list[e][1] == cur_y:
        e += 1
    row_ranges.append((s, e))
    s = e

row_cnt = len(row_ranges)

for top in range(row_cnt):
    # sum, Lmax, Rmax, Tmax
    seg_tree_sum = [0] * (added_length * 2)
    seg_tree_Lmax = [0] * (added_length * 2)
    seg_tree_Rmax = [0] * (added_length * 2)
    seg_tree_Tmax = [0] * (added_length * 2)

    for bottom in range(top, row_cnt):
        start, end = row_ranges[bottom]

        # 이번 bottom 행의 점들을 x축 세그트리에 추가
        for pointer in range(start, end):
            x_idx, y_idx, w = ordered_list[pointer]
            m = x_idx + added_length

            # 리프 갱신
            seg_tree_sum[m] += w
            seg_tree_Lmax[m] = seg_tree_sum[m]
            seg_tree_Rmax[m] = seg_tree_sum[m]
            seg_tree_Tmax[m] = seg_tree_sum[m]

            # 부모 갱신
            while m > 1:
                if m % 2 == 1:
                    left = m - 1
                    right = m
                else:
                    left = m
                    right = m + 1

                parent = m // 2

                seg_tree_sum[parent] = seg_tree_sum[left] + seg_tree_sum[right]
                seg_tree_Lmax[parent] = max(seg_tree_Lmax[left], seg_tree_sum[left] + seg_tree_Lmax[right])
                seg_tree_Rmax[parent] = max(seg_tree_Rmax[right], seg_tree_Rmax[left] + seg_tree_sum[right])
                seg_tree_Tmax[parent] = max(seg_tree_Tmax[left], seg_tree_Tmax[right], seg_tree_Rmax[left] + seg_tree_Lmax[right])

                m //= 2

        # 현재 [top .. bottom] y구간에서의 최대 x연속합
        if max_advantage < seg_tree_Tmax[1]:
            max_advantage = seg_tree_Tmax[1]

print(max_advantage)
