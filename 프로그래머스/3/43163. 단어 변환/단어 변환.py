def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)
    answer = 51

    def dfs(curr_word, depth):
        nonlocal answer

        if curr_word == target:
            answer = min(answer, depth)
            return

        if depth >= answer:
            return

        for i in range(len(words)):
            if not visited[i] and is_valid(curr_word, words[i]):
                visited[i] = True
                dfs(words[i], depth + 1)
                visited[i] = False

    dfs(begin, 0)

    return answer if answer != 51 else 0


def is_valid(a, b):
    diff = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1

        if diff > 1:
            return False

    return diff == 1