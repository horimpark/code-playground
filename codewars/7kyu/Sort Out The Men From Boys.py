def men_from_boys(arr):
    evens = sorted(list(set([a for a in arr if not a % 2])))
    odds = sorted(list(set(arr) - set(evens)), reverse=True)
    return evens + odds
