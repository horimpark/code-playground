from re import search


def catalog(s, article):
    lines = []
    for line in s.split("\n"):
        if article in line:
            name = search(f"<name>(.*)</name>", line).group(1)
            number = search(f"<qty>(.*)</qty>", line).group(1)
            price = search(f"<prx>(.*)</prx>", line).group(1)
            lines.append(f"{name} > prx: ${price} qty: {number}")
    return "\r\n".join(lines) if lines else "Nothing"
