def drop_dup(arr):
    seen = set()
    answer = []
    for a in arr:
        if a not in seen:
            answer.append(a)
            seen.add(a)
    return answer


def remove_duplicate_ids(obj):
    obj = dict(sorted(obj.items(), key=lambda x: int(x[0])))
    new_obj = {}
    for idx, (num, list_) in enumerate(obj.items()):
        over = list(obj.values())[idx+1:]
        if over:
            if len(over) > 1:
                over = [i for o in over for i in o]
            else:
                over = over[0]
            over = set(over)
            new_list = [l for l in list_ if l not in over]
        else:
            new_list = list_
        new_obj[num] = new_list
    new_obj = {k: drop_dup(v) for k, v in new_obj.items()}
    return new_obj