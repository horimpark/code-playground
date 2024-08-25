def printer_error(s):
    return '{}/{}'.format(len([c for c in s if c not in 'abcdefghijklm']), len(s))


if __name__ == "__main__":
    print(printer_error("aaabbbbhaijjjm"))  # 0/14