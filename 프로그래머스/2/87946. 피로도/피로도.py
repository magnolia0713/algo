

def solution(k, dungeons):
    
    visited = [0] * len(dungeons)

    # dfs 완전탐색 : 경우의수가 8! 이내 => 완탐가능
    def recursion(k, depth):
    
        if depth >= len(dungeons):
            return depth
        
        # 전역변수 최소화
        x = depth   

        for i in range(len(dungeons)):

            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = 1
                y = recursion(k - dungeons[i][1], depth+1)
                visited[i] = 0
                if x < y:
                    x = y

        return x
    
    answer = recursion(k, 0)
        
    return answer


        
        