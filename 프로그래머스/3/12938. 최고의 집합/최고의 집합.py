def solution(n, s):
    answer = []
    
    # 1만으로도 합을 표현할 수 없는 경우 answer = -1
    if n > s:
        return [-1]
    
    opt_x, remained = divmod(s, n)
    
    value_1 = opt_x
    for _ in range(n - remained):
        answer.append(opt_x)
        
    for _ in range(remained):
        answer.append(opt_x + 1)
        
    return answer