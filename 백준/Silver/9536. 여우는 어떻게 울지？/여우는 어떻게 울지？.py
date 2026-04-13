test_case = int(input())

for _ in range(test_case):
    a_set = set()
    #쿼리 리스트 미리 뺴놓고 다른 동물소리 먼저 받기
    query_list = list(input().split())

    # 단어 집어넣기
    while True:
        words = list(input().split())
        if words[1] == 'does':
            break
        else:
            a_set.add(words[2])


    ans = []

    for word in query_list:
        if word in a_set:
            continue

        else:
            ans.append(word)

    print(*ans)
