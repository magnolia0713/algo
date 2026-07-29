def solution(k, tangerine):
    
    from collections import defaultdict
    answer = 0
    
    # 자료구조를 딕셔너리에 담고, 수를 더함
    
    tangerine_size = defaultdict(int)
    sorted_size_num = [] # (갯수, 사이즈)
    for i in tangerine:
        tangerine_size[i] += 1
        
    for size, quantity in tangerine_size.items():
        sorted_size_num.append((quantity, size))
    
    # 갯수순으로 역정렬
    sorted_size_num.sort(key=lambda x:-x[0])
    
    idx = 0
    while k > 0:
        k -= sorted_size_num[idx][0]
        idx += 1
        answer += 1
        
    return answer