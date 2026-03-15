T = int(input())

def over_avg(stu_number, grade):
    avg = sum(grade) / stu_number
    counter = 0
    for i in grade:
        if i > avg:
            counter += 1
    
    return counter/stu_number * 100

for i in range(T):
    grade_number, *grade = map(int, input().split())
    print(f'{over_avg(grade_number, grade):.3f}%')