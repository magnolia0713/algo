def solution(n, stations, w):
    
    stations.sort()
    
    # 우선 처음에 있는 곳은 0부터 시작이므로 처음과 마지막은 분리해서 계산.
    
    # 처음
    if stations[0] - w > 0:
        x = (stations[0] - w - 2) // (2*w + 1) + 1
    else:
        x = 0
        
    # 마지막
    if n - stations[-1] - w > 0:
        z = (n - stations[-1] - w - 1) // (2*w + 1) + 1
    else:
        z = 0
    # 중간
    y = 0
    for i in range(len(stations) - 1):
        
        dist = stations[i+1] - stations[i]
        if dist > 2 * w:
            y += (dist - 2*w - 2) // (2*w+1) + 1

    
    answer = x + y + z
    
    
    return answer