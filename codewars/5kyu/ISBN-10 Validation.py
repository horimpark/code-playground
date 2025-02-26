def valid_ISBN10(isbn):
    if len(isbn) != 10 or not (
        isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == "X")
    ):
        return False
    res = sum(i * (10 if x == "X" else int(x)) for i, x in enumerate(isbn, 1))
    return True if res % 11 == 0 else False
