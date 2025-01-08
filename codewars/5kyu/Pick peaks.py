def pick_peaks(arr):
    res = {"pos": [], "peaks": []}
    for x in range(1, len(arr) - 1):
        if arr[x] > arr[x - 1] and arr[x] > arr[x + 1]:
            res["pos"].append(x)
            res["peaks"].append(arr[x])
        elif arr[x] > arr[x - 1] and arr[x] >= arr[x + 1]:
            for y in range(x + 1, len(arr)):
                if arr[y] < arr[x]:
                    res["pos"].append(x)
                    res["peaks"].append(arr[x])
                    break
                elif arr[y] > arr[x]:
                    break

    return res
