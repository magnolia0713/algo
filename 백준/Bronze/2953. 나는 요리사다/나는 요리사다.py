max_total = 0

pt_number = 0

max_pt = 0

while True:
    try:
        a, b, c, d = map(int, input().split())
        total = a + b + c + d
        pt_number += 1

        if total > max_total:
            max_total = total
            max_pt = pt_number


    except:
        break

print(max_pt, max_total)