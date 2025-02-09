def is_triangle(a, b, c):
    all_lines = [a, b, c]
    max_ = max(all_lines)
    all_lines.remove(max_)

    if sum(all_lines) > max_:
        return True
    else:
        return False