from preloaded import MORSE_CODE


def all_space_variants(s: str) -> list[str]:
    n = len(s)
    if n <= 1:
        return [s]

    results = []
    for mask in range(1 << (n - 1)):
        parts = [s[0]]
        for i in range(n - 1):
            if mask & (1 << i):
                parts.append(" ")
            parts.append(s[i + 1])
        results.append("".join(parts))

    return results


def possible_words(morse_str: str) -> set[str]:
    res = set()

    for x in all_space_variants(morse_str):
        tokens = x.split(" ")
        if all(t in MORSE_CODE for t in tokens):
            res.add("".join(MORSE_CODE[t] for t in tokens))
    res.discard("")
    return res
