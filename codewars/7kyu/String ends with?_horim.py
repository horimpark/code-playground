def solution(text, ending):
    return True if text[-len(ending):] == ending else False
