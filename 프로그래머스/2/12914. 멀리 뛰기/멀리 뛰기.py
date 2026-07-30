def solution(n):
    
    # 전형적인 dp 문제 => 위의 답을 아래 계산을 통해 도출 가능
    
    answer_arr = [0] * (n+1)
    
    answer_arr[1] = 1
    if n >= 2:
        answer_arr[2] = 2
    
    # dp 배열로 상위정답 도출
    for i in range(3, n+1):
        answer_arr[i] = (answer_arr[i-1] + answer_arr[i-2]) % 1234567
    
    return answer_arr[n]