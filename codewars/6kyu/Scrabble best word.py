def get_best_word(points, words):
    score_book = {chr(i): points[idx] for idx, i in enumerate(range(ord('A'), ord('Z') + 1))}

    scores = []
    for word in words:
        score = 0
        for w in word:
            score += score_book[w]
        scores.append(score)

    min_scores = [x * len(words[idx]) if x == max(scores) else 0 for idx, x in enumerate(scores)]

    return min_scores.index(min([x for x in min_scores if x != 0]))