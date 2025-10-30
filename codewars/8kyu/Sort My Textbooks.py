def sorter(textbooks):
    lower_dict = {x: x.lower() for x in textbooks}
    sorted_books = sorted(lower_dict.items(), key=lambda x: x[1])
    return [x[0] for x in sorted_books]
