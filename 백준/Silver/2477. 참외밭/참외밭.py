K = int(input())
value_list = []

for i in range(6):
    key, value = map(int,input().split())
    value_list.append(value)

# 최대 변의 길이를 찾기 위한 동작

len_a = int(sum(value_list[::2]) / 2)
len_b = int(sum(value_list[1::2]) / 2)

#최대 변의 길이를 구함으로써 최대 길이의 변의 길이가 몇번쨰 순서인지 역추적
temp_len_a = value_list[::2]
temp_len_b = value_list[1::2]

index_len_a = temp_len_a.index(len_a)
index_len_b = temp_len_b.index(len_b)

index_len_a = index_len_a * 2
index_len_b = index_len_b * 2 + 1

#길이가 가장 긴 변의 두변이 서로 붙어있으면 붙어있는 다른 두변의 길이는 긴 변에서 그 두 변의 길이를 뺀 것과 같음.

# if는 리스트의 마지막 열 5열에 데이터가 걸쳤을 때 따로 해석하기 위한 동작.
if index_len_a - index_len_b == 1 or index_len_a - index_len_b == -5:
    if index_len_a == 5:
        index_len_c = 0
        index_len_d = 3
        
    else:
        index_len_c = index_len_a + 1
        index_len_d = index_len_b - 1
    
else:
    if index_len_b == 5:
        index_len_c = 3
        index_len_d = 0
    else:
        index_len_c = index_len_a - 1
        index_len_d = index_len_b + 1

# 변의 길이가 가로든 세로든 상관없이 정할 수 있음. 도형이 회전하는 것으로 변의 넓이는 변하지 않음.

# 큰 넓이에서 작은 넓이를 뺴는 과정.
max_area = len_a * len_b

len_c = value_list[index_len_c]
len_d = value_list[index_len_d]


min_area = (len_a - len_d) * (len_b - len_c)

total_area = max_area - min_area

total = total_area * K 
print(int(total))