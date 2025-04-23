def validate_sequence(sequence):
    gap = sequence[1] - sequence[0]
    return sequence == sorted(sequence) and [i for i in range(min(sequence), max(sequence)+1, gap)] == sequence