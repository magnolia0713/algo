n, m = map(int, input().split())
n_set = set(map(int, input().split()))
m_set = set(map(int, input().split()))
result = n_set - m_set
print(len(result))
print(*sorted(result))