import re


def solve(s):
    scores = {x: i + 1 for i, x in enumerate("abcdefghijklmnopqrstuvwxyz")}
    result = re.split("[aeiou]", s)
    result = [segment for segment in result if segment]
    cnt = []
    for word in result:
        score = 0
        for x in word:
            score += scores[x]
        cnt.append(score)
    return max(cnt)
