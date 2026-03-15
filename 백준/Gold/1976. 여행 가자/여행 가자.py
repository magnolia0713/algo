
def linked_family(start):

    basket = [start]
    storage = {start}
    while basket:
        location = basket.pop()
        for i in range(n):
            if matrix[location][i] and i not in storage:
                storage.add(i)
                basket.append(i)


    for i in range(1,m):
        if visit_list[i] not in storage:
            return 'NO'
    else:
        return 'YES'


    return


n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
visit_list = list(map(int, input().split()))

for i in range(m):
    visit_list[i] -= 1

print(linked_family(visit_list[0]))
