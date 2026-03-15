working_set = set()

n = int(input())

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        working_set.add(name)

    else:
        working_set.remove(name)

working_list = list(working_set)

working_list.sort(reverse=True)

print(*working_list, sep = '\n')