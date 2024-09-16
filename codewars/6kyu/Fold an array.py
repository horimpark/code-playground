def fold_array(array, runs):
    for _ in range(runs):
        thrs = int(len(array) / 2)
        answer = []
        for i in range(thrs):
            answer.append(array[i] + array[-(i + 1)])
        if len(array) % 2:
            answer.append(array[thrs])
        array = answer

    return answer


if __name__ == "__main__":
    fold_array([1, 2, 3, 4, 5], 1)  # [6, 6, 3]