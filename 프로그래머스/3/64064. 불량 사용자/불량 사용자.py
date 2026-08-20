# user_id의 배열 크기가 8 이하이므로 dfs로 접근한다.

def solution(user_id, banned_id):
    # 2차원배열로 미리 banned_id가 가능한 부분을 매핑한다.
    
    
    possible_ban = [[] for _ in range(len(banned_id))]
    
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            
            if len(banned_id[i]) == len(user_id[j]):
                check = True
                
                for k in range(len(banned_id[i])):
                    if banned_id[i][k] != '*' and banned_id[i][k] != user_id[j][k]:
                        check = False
                        break
                
                if check:
                    possible_ban[i].append(j)
    
    # dfs 시작
    answer = set()
    visited = [0] * len(user_id)

    def dfs(depth, memo):
        
        nonlocal answer
        
        if depth == len(banned_id): 
            answer.add(tuple(sorted(memo)))
            return
        

        for i in possible_ban[depth]:
            if not visited[i]:
                visited[i] = 1
                memo.append(i)
                dfs(depth+1, memo)
                visited[i] = 0
                memo.pop()
                    
    dfs(0, [])
    
    return len(answer)