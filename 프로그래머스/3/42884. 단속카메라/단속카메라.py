def solution(routes):
    routes.sort(key=lambda x: x[1])

    answer = 1
    
    # pointer_a: 검사할 차량
    # pointer_b: 현재 카메라를 설치한 기준 차량
    pointer_a = 1
    pointer_b = 0
    
    while pointer_a < len(routes):

        camera_position = routes[pointer_b][1]

        # 현재 카메라가 해당 차량의 진입점보다 뒤에 있으면 단속 가능
        if camera_position >= routes[pointer_a][0]:
            pointer_a += 1

        # 현재 카메라로 단속할 수 없다면 새 카메라 설치
        else:
            pointer_b = pointer_a
            pointer_a += 1
            answer += 1

    return answer