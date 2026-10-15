def solution(stones, k):
    
    # 평균값부터 이분탐색 시작
    top = max(stones)
    bot = 1
    
    while bot < top:
        mid = (bot + top + 1) // 2
        cnt = 0
        
        for i in stones:
            if i < mid:
                cnt += 1
                if cnt >= k:
                    top = mid - 1 
                    break
            else:
                cnt = 0
        
        else:
            bot = mid
            
    return bot