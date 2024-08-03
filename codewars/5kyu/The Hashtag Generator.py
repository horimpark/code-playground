def generate_hashtag(s):
    if not s:
        return False
    result = "#" + "".join([f"{x[0].upper()}{x[1:].lower()}" for x in s.split()])
    if len(result) > 140:
        return False
    else:
        return result
