def solution(text, ending):
    return any(ending == text[-l:] for l in range(len(text)))


if __name__ == "__main__":
    solution("abcde", "cde")  # True