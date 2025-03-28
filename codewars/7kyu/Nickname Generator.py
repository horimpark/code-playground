def nickname_generator(name):
    vowels = "aeiou"
    if len(name) <= 3:
        return 'Error: Name too short'
    if name[2] not in vowels:
        return name[:3]
    if name[2] in vowels:
        return name[:4]

    return ""