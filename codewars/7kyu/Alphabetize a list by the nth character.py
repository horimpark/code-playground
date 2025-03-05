def sort_it(words, n):
    w_list = words.split(", ")
    words = sorted(w_list, key=lambda x: x[n-1])
    return ", ".join(words)