n = int(input())

n_list = list(map(int, input().split()))
n_list.sort()
#print(n_list)
a_min = 1e11
for i in range(n):

    if not a_min:
        break

    m_list = n_list[:i] + n_list[i+1:]

    head = 0
    tail = n-2
    while head != tail:
        temp = m_list[head] + m_list[tail] + n_list[i]

        if a_min > abs(temp):
            a_min = abs(temp)
            candidate = [n_list[i], m_list[head], m_list[tail]]
        if temp < 0:
            head += 1

        elif temp > 0:
            tail -= 1

        else:
            break

print(*sorted(candidate))