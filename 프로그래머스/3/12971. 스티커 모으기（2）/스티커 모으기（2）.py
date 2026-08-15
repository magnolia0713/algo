def solution(sticker):
    answer = 0
    
    if len(sticker) <= 2:
        return max(sticker)
        
    dp_1 = [0] * len(sticker)
    dp_2 = [0] * len(sticker)
    
    dp_1[0] = dp_1[1] = sticker[0]
    dp_2[1] = sticker[1]
    
    
    
    for i in range(2, len(sticker)):
        dp_1[i] = max(dp_1[i-1], dp_1[i-2] + sticker[i])
        dp_2[i] = max(dp_2[i-1], dp_2[i-2] + sticker[i])
        

    return max(dp_1[len(sticker)-2], dp_2[len(sticker)-1])