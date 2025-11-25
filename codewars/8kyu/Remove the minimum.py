def remove_smallest(numbers):
    if not numbers:
        return []
    min_idx = numbers.index(min(numbers))
    return [numbers[i] for i in range(len(numbers)) if i != min_idx]
