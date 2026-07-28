def solution(genres, plays):
    answer = []
    
    # 목록별 재생 수를 계산할 때 필요한 자료구조
    from collections import defaultdict
    
    # 목록 내 재생순위를 매기기 위한 자료구조
    from heapq import heappush, heappop
    
    # 자료구조 생성
    total_play = defaultdict(int)
    genre_play = defaultdict(list) # { genre: heap[] }
    
    for i in range(len(genres)):
        # 장르별 누계에 더해준다.
        total_play[genres[i]] += plays[i]
        # (-재생 횟수, id)
        heappush(genre_play[genres[i]], (-plays[i], i))
        
    # sorting을 위한 배열 준비
    total_play_arr = []
    
    for genre, cnt in total_play.items():
        total_play_arr.append((cnt, genre))
    
    # 조회수 많은 순서
    total_play_arr.sort(key=lambda x:-x[0])
    for cnt, genre in total_play_arr:
        if cnt:
            answer.append(genre_play[genre][0][1])
            if len(genre_play[genre]) > 1:
                heappop(genre_play[genre])
                answer.append(genre_play[genre][0][1])
    
    return answer