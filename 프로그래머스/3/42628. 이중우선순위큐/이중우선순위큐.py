from heapq import heappush, heappop

def solution(operations):
    max_list = []
    min_list = []
    ids = [0] * 1000001
    id = 0
    for orders in operations:
        order, num = orders.split()
        num = int(num)
        # 값 입력
        if order == 'I':
            heappush(max_list, (-num, id))
            heappush(min_list, (num, id))

            ids[id] = 1
            id += 1
        # 최대값 삭제
        elif order == 'D' and num == 1:
            # 최대힙에서 빼는데, 그 전에 죽은 노드 처리
            # 죽은노드가 아닐 때 까지 뽑음.
            while max_list:
                num, idx = heappop(max_list)
                # 살아있는 노드였다면
                if ids[idx]:
                    ids[idx] = 0
                    break
                else:
                    continue

        # 최소값 삭제
        else:
            # 최대힙에서 빼는데, 그 전에 죽은 노드 처리
            # 죽은노드가 아닐 때 까지 뽑음.
            while min_list:
                num, idx = heappop(min_list)
                # 살아있는 노드였다면
                if ids[idx]:
                    ids[idx] = 0
                    break
                else:
                    continue
        #print(ids[:10])

    min_ans = 0
    max_ans = 0
    while max_list:
        temp, idx = heappop(max_list)
        if ids[idx]:
            max_ans = -temp
            break

    while min_list:
        temp, idx = heappop(min_list)
        if ids[idx]:
            min_ans = temp
            break
    return [max_ans, min_ans]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))