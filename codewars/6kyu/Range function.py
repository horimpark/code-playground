def range_function(*args):
    arg_length = len(args)

    if arg_length == 1:
        start, step, end = 1, 1, args[0]
    elif arg_length == 2:
        start, step, end = args[0], 1, args[1]
    elif arg_length == 3:
        start, step, end = args[0], args[1], args[2]

    cur = start
    while cur <= end:
        yield cur
        cur += step
