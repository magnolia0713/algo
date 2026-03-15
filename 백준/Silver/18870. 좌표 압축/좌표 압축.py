import sys
print = sys.stdout.write

N = int(input())
a_list = list(map(int, input().split()))
a_set = set(a_list)
sorted_list = sorted(list(a_set))
a_dict = {}
for i in range(len(a_set)):
    a_dict[sorted_list[i]] = i

for i in range(N):
    a_list[i] = a_dict[a_list[i]]
print(' '.join(map(str, a_list)))