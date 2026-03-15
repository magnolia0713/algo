dict_grade = {'A+' : 4.5,
              'A0' : 4.0,
              'B+' : 3.5,
              'B0' : 3.0,
              'C+' : 2.5,
              'C0' : 2.0,
              'D+' : 1.5,
              'D0' : 1.0,
              'F'  : 0.0
}
total_credits = 0.0
list_grade = []

for _ in range(20):
    subject, credits, grade = input().split()
    if grade == 'P':
        continue

    total_credits += float(credits)
    list_grade.append(dict_grade[grade] * float(credits))


final_grade = sum(list_grade) / total_credits

print(f"{final_grade:.5f}")
