def letters_to_numbers(s):
    sum = 0
    score_dict = {x:i+1 for i, x in enumerate('abcdefghijklmnopqrstuvwxyz')}
    for x in s:
        if x.isalpha():
            if x.islower():
                sum += score_dict[x]
            else:
                sum += score_dict[x.lower()]*2
        elif x.isdigit():
            sum += int(x)
        else:
            continue
    return sum

        