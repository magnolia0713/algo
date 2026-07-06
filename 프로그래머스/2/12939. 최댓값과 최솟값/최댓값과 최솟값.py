def solution(s):
    
    answer = list(map(int, s.split()))
    answer.sort()
    result = str(answer[0]) + ' ' + str(answer[-1])
    return result