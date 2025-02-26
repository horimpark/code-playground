def title_case(title, minor_words=""):
    m_words = [x.lower() for x in minor_words.split(" ")]
    t_words = [x.lower() for x in title.split(" ")]

    res = []
    for x in t_words:
        if x.lower() in m_words:
            res.append(x)
        else:
            res.append(f"{x[0].upper()}{x[1:].lower()}")
    res = " ".join(res)
    return f"{res[0].upper()}{res[1:]}" if res else ""


def title_case(title, minor_words=""):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return " ".join(
        [word if word in minor_words else word.capitalize() for word in title]
    )
