

def dfs(depth):
    global total_count

    if depth == n:
        total_count += 1
        return

    for i in range(len(num_list)):
        p = num_list[i]
        if depth + p not in plus_dir and depth - p not in minus_dir:
            plus_dir.add(depth + p)
            minus_dir.add(depth - p)
            temp = num_list.pop(i)
            dfs(depth + 1)
            num_list.insert(i, temp)
            plus_dir.remove(depth + p)
            minus_dir.remove(depth - p)



n = int(input())
total_count = 0
num_list = list(range(0, n))
plus_dir = set()
minus_dir = set()
dfs(0)
print(total_count)