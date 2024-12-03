objects = {
    "bw": 'road',
    "bwsg": 'settlement',
    "ooogg": 'city',
    "osg": 'development'
}


def build_or_buy(hand):
    results = []
    for key, object in objects.items():
        key = [k for k in key]
        hand_set = [h for h in hand]
        for hs in hand_set:
            if hs in key:
                key.remove(hs)
        if len(key) == 0:
            results.append(object)
    return results


if __name__ == "__main__":
    print(build_or_buy("bwsg"))  # ['road', 'settlement', 'city', 'development']
    print(build_or_buy("bwosg"))  # ['road', 'settlement', 'development']
