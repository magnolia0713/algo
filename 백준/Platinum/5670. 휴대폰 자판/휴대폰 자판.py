import sys
input = sys.stdin.readline

# 일단 트리를 먼저 구축하자.
while True:
    line = input().rstrip()
    if not line:
        break

    n = int(line)
    trie = {
        'children': {},
        'mark': False,
    }
    total_cnt = 0

    for _ in range(n):
        word = input().rstrip()
        pointer = trie

        # 마지막 노드만 제외하고 우선 로직 구성
        for idx in range(len(word)-1):
            if word[idx] not in pointer['children']:
                pointer['children'][word[idx]] = {
                    'children': {},
                    'mark': False,
                }
            pointer = pointer['children'][word[idx]]

        # 마지막 노드 처리
        if word[-1] not in pointer['children']:
            pointer['children'][word[-1]] = {
                'children': {},
                'mark': True
            }
        else:
            pointer['children'][word[-1]]['mark'] = True
        pointer = pointer['children'][word[-1]]

    # 문제의 답은 dfs로 구해야 할 듯 하다.
    # 길을 가는데 외길이면 0, 외길이 아니면 1 추가하면 되겠네.

    def dfs(node, cnt):
        nonlocal_total_cnt[0]

        # 끝노드일 때 해당 값 합산
        if node['mark']:
            nonlocal_total_cnt[0] += cnt

        for char in node['children']:
            child = node['children'][char]

            # 첫 글자이거나, 현재 노드가 단어의 끝이거나, 갈림길이면 입력 필요
            if node is trie or node['mark'] or len(node['children']) > 1:
                dfs(child, cnt + 1)
            else:
                dfs(child, cnt)

    nonlocal_total_cnt = [0]
    dfs(trie, 0)
    print(f"{nonlocal_total_cnt[0] / n:.2f}")