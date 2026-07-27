def solution(record):
    answer = []
    a_dict = {}
    orders = []

    for log in record:
        data = log.split()
        status = data[0]
        uid = data[1]

        if status == 'Enter':
            nickname = data[2]
            a_dict[uid] = nickname
            orders.append((uid, 1))

        elif status == 'Leave':
            orders.append((uid, 2))

        elif status == 'Change':
            nickname = data[2]
            a_dict[uid] = nickname

    for a_id, status in orders:
        if status == 1:
            answer.append(f"{a_dict[a_id]}님이 들어왔습니다.")
        else:
            answer.append(f"{a_dict[a_id]}님이 나갔습니다.")

    return answer