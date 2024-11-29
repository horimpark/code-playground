def string_expansion(s):
    result = ""
    num = 1
    alpha = []
    for idx, i in enumerate(s):
        if i.isdigit():
            if alpha:
                for a in alpha:
                    for _ in range(int(num)):
                        result += a
                alpha = []
            num = i
        elif i.isalpha():
            alpha.append(i)
            if idx == len(s) - 1:
                for a in alpha:
                    for _ in range(int(num)):
                        result += a

    return result


if __name__ == "__main__":
    print(string_expansion('3D2a5d2f'))  # "DDDaadddddff"
    print(string_expansion('3d332f2a'))  # "dddffaa"
    print(string_expansion('abcde'))  # "abcde