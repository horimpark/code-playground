def series_sum(n):
    if n == 0:
        return "0.00"
    answer = str(round(sum([1/(4+3*(x-1)) for x in range(n)]), 2))
    sa = answer.split(".")
    if len(sa[-1]) < 2:
        answer += "0"
    return answer


def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))