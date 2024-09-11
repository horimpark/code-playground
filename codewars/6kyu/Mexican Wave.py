def wave(people):
    people = people.lower()

    c_idx = [i for i, x in enumerate(people) if x.isalpha()]
    result = []

    for x in c_idx:
        if x == 0:
            result.append(f"{people[x].upper()}{people[x+1:]}")
        elif x == c_idx[-1]:
            result.append(f"{people[:x]}{people[x].upper()}{people[x+1:]}")
        else:
            result.append(f"{people[:x]}{people[x].upper()}{people[x+1:]}")
    return result