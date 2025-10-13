def sequence_sum(begin, end, step):
    if (begin > end and step > 0) or (begin < end and step < 0):
        return 0
    
    n = ((end - begin) // step) + 1 if step != 0 else 0
    last = begin + (n - 1) * step

    return n * (begin + last) // 2 if n > 0 else 0