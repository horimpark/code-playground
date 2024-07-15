def format_duration(seconds):
    if seconds == 0:
        return "now"
    check = [60 * 60 * 24 * 365, 60 * 60 * 24, 60 * 60, 60]
    result_time = [0, 0, 0, 0, 0]

    remain = seconds

    for i, y in enumerate(check):
        if remain // y > 0:
            result_time[i] = remain // y
            remain = remain % y
    result_time[-1] = remain

    t_words = ["year", "day", "hour", "minute", "second"]
    result = []
    for x, y in zip(result_time, t_words):
        if x == 0:
            continue
        elif x == 1:
            result.append(f"{x} {y}")
        else:
            result.append(f"{x} {y}s")

    if len(result) == 1:
        return result[0]
    else:
        last = ""
        for x in result:
            if x == result[-2]:
                last += f"{x} and "
            elif x == result[-1]:
                last += x
            else:
                last += f"{x}, "
        return last


print(format_duration(3599))
print(format_duration(86399))
print(format_duration(59))
print(format_duration(60))
print(format_duration(132030240))
print(format_duration(205851834))
