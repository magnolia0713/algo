n = int(input())

# 딱히 cnt를 세거나, 노드가 있는지 확인할 필요가 없다.
trie = {
    'children': {},
}

for _ in range(n):
    pointer = trie
    directions = list(input().split('\\'))

    for direction in directions:
        if direction not in pointer['children']:
            pointer['children'][direction] = {
                'children': {}
            }
        pointer = pointer['children'][direction]

# dfs 사전순으로 출력해보자.
answer_sheet = []
def dfs(node, cnt):
    keys = []
    for child in node['children'].keys():
        keys.append(child)
    keys.sort()
    for nxt_node in keys:
        answer_sheet.append((nxt_node, cnt))
        dfs(node['children'][nxt_node], cnt + 1)

ans = dfs(trie, 0)
for direction, space in answer_sheet:
    print(' '*space + direction)