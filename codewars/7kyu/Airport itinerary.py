def itinerary(travel):
    res = []
    for x in travel:
        if not res or x["in"] != res[-1]:
            res.append(x["in"])
        if not res or x["out"] != res[-1]:
            res.append(x["out"])
    return "-".join(res)
