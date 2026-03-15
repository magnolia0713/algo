N = int(input())
referred_user = int(input())
referred_list = list(map(int,input().split()))

def candidate_sorting(N, referred_user, referred_list):
    
    candidate_list = []
    for i in range(referred_user):
        updated = False
        
        for j in candidate_list:
            if referred_list[i] == j[0]:
                j[1] += 1
                updated = True
                break
                
        if not updated:
            
            if len(candidate_list) < N:
                candidate_list.append([referred_list[i], 1, i])

            else:
                min_a = min(range(N), key=lambda k: (candidate_list[k][1], candidate_list[k][2]))

                candidate_list[min_a] = [referred_list[i], 1, i]
    final_list = []    
    
    for l in range(len(candidate_list)):
        final_list.append(candidate_list[l][0])

    final_list.sort()
    return(final_list)

result = candidate_sorting(N, referred_user, referred_list)

print(*result)