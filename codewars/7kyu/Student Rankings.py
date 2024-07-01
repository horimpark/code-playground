def post_grades(students):
    person2scores = dict()
    for x in students:
        split_x = x.split(" - ")
        s_id, scores = split_x[0], [float(x) for x in split_x[2].split(" ")]
        person2scores[s_id] = sum(scores) / len(scores)

    sorted_p2s = sorted(person2scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_p2s
