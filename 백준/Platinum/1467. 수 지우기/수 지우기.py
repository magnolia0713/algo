import sys

# 입력 처리
input_data = sys.stdin.read().split()

if input_data:
    S = input_data[0]
    R = input_data[1] if len(input_data) > 1 else ""

    # 각 숫자의 등장 횟수 카운트
    count_S = [0] * 10
    count_R = [0] * 10

    for char in S:
        count_S[int(char)] += 1
    for char in R:
        count_R[int(char)] += 1

    # 남겨야 할 숫자의 개수 계산
    count_K = [count_S[i] - count_R[i] for i in range(10)]

    ans = []
    start_idx = 0
    total_K = len(S) - len(R)  # 최종적으로 찾아야 할 숫자의 총 길이

    # 그리디 탐색 시작
    while total_K > 0:
        # 가장 큰 숫자 9부터 0까지 확인
        for d in range(9, -1, -1):
            if count_K[d] == 0:
                continue

            # start_idx 이후 처음으로 등장하는 d의 위치 찾기
            idx = S.find(str(d), start_idx)
            if idx == -1:
                continue

            is_valid = True
            temp_R = count_R[:]

            # start_idx부터 idx 이전까지의 숫자를 모두 지울 수 있는지 확인
            for i in range(start_idx, idx):
                num = int(S[i])
                if temp_R[num] == 0:
                    is_valid = False
                    break
                temp_R[num] -= 1

            # 지울 수 있다면 해당 숫자를 선택
            if is_valid:
                ans.append(str(d))
                count_K[d] -= 1

                # 지나친 숫자들을 실제 지울 숫자 카운트에서 차감
                for i in range(start_idx, idx):
                    count_R[int(S[i])] -= 1

                start_idx = idx + 1
                total_K -= 1
                break  # 다음 자리 숫자를 찾기 위해 루프 탈출

    # 결과 출력
    print("".join(ans))