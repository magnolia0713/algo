T = int(input())

total_number = 0
set_people = set()

for t in range(T):
    a = input()
    if a == 'ENTER':
        total_number += len(set_people)
        set_people.clear()

    else:
        set_people.add(a)

total_number += len(set_people)

print(total_number)