def solution(gems):
    from collections import defaultdict

    full_cnt = len(set(gems))

    gem_cnt = defaultdict(int)
    cnt = 0
    s = 0

    min_len = len(gems) + 1
    answer = [0, len(gems) - 1]

    for e in range(len(gems)):
        gem_cnt[gems[e]] += 1

        if gem_cnt[gems[e]] == 1:
            cnt += 1

        # 모든 종류가 들어왔으면 왼쪽을 최대한 줄임
        while cnt == full_cnt:

            if e - s + 1 < min_len:
                min_len = e - s + 1
                answer = [s, e]

            gem_cnt[gems[s]] -= 1

            if gem_cnt[gems[s]] == 0:
                cnt -= 1

            s += 1

    # 문제에서는 1-based index
    return [answer[0] + 1, answer[1] + 1]