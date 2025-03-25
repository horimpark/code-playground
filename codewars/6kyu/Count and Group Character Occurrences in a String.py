from collections import Counter, defaultdict


def get_char_count(s):
    s_counter = Counter(s.lower())
    answer = defaultdict(list)
    for c, n in s_counter.items():
        if c.isalpha() or c.isdigit():
            answer[n].append(c)
    answer = {k: sorted(v) for k, v in answer.items()}
    return dict(sorted(answer.items(), reverse=True))