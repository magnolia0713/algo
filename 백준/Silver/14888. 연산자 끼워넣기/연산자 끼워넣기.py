def dfs(depth, result):
    if depth == len(num_list):
        result_set.add(result)
        return

    for i in range(4):
        if a_list[i] != 0:
            a_list[i] -= 1
            if i == 0:
                dfs(depth + 1, result + num_list[depth])
            elif i == 1:
                dfs(depth + 1, result - num_list[depth])
            elif i == 2:
                dfs(depth + 1, result * num_list[depth])
            else:
                if result < 0:
                    dfs(depth + 1, -(-result // num_list[depth]))
                else:
                    dfs(depth + 1, result // num_list[depth])
            a_list[i] += 1



N = int(input())
num_list = list(map(int, input().split()))
a_list = list(map(int, input().split()))
result_set = set()
dfs(1, num_list[0])

print(max(result_set))
print(min(result_set))