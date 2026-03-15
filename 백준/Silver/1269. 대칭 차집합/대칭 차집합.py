n, m = map(int, input().split())

m_set = set(map(int, input().split()))
n_set = set(map(int, input().split()))

a_set = m_set - n_set ; b_set = n_set - m_set

print(len(a_set) + len(b_set))