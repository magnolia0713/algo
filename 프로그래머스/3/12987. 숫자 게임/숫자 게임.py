def solution(A, B):
    A.sort(); B.sort()
    
    pointer = 0
    answer = 0  
    
    for i in A:
        if pointer >= len(B):
            break
            
        if B[pointer] <= i:
            while pointer < len(B):
                
                if B[pointer] <= i:
                    pointer += 1
                    
                else:
                    pointer += 1
                    answer += 1
                    break
        else:
            pointer += 1
            answer += 1
                    

    return answer