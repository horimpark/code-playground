def unique_in_order(sequence):
    answer = []
    current = None
    for s in sequence:
        if current != s:
            answer.append(s)
            current = s
    return answer


if __name__=="__main__":
    print(unique_in_order('AAAABBBCCDAABBB'))  # ['A', 'B', 'C', 'D', 'A', 'B']