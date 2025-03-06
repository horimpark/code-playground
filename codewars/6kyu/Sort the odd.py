def sort_array(source_array):
    if not source_array:
        return source_array
    odd = [x for x in source_array if x % 2 != 0]
    even = [x if x % 2 == 0 else -1 for x in source_array]
    sort_odd = sorted(odd)

    result = []
    cnt = 0
    for x in even:
        if x == -1:
            result.append(sort_odd[cnt])
            cnt += 1
        else:
            result.append(x)
    return result


# def sort_array(arr):
#   odds = sorted((x for x in arr if x%2 != 0), reverse=True)
#   return [x if x%2==0 else odds.pop() for x in arr]

def sort_array(source_array):
    if not source_array:
        return []
    index_ = [i for i, s in enumerate(source_array) if s % 2]
    nums_ = [s for i, s in enumerate(source_array) if s % 2]
    nums_ = sorted(nums_)

    idx_to_num = {i: n for i, n in zip(index_, nums_)}

    answer = []
    for i, s in enumerate(source_array):
        answer.append(idx_to_num.get(i, s))

    return answer
