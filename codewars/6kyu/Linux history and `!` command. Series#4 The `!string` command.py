def bang_start_string(n, history):
    lines = history.strip().split('\n')

    for line in reversed(lines):
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2:
            _, command = parts
            if command.startswith(n):
                return command

    return f"!{n}: event not found"
