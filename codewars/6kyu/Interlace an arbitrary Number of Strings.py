def combine_strings(*args):
    res = [x[0] for x in zip(args)]
    if not res:
        return ""
    max_length = max([len(x) for x in res])

    print(res)
    result = []
    for x in range(max_length):
        for y in range(len(res)):
            if len(res[y]) - 1 >= x:
                result.append(res[y][x])
            else:
                result.append("")

    return "".join(result)


# from itertools import zip_longest
#
# def combine_strings(*args):
#     return ''.join(map(''.join, zip_longest(*args, fillvalue='')))
