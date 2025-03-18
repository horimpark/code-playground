def replace_all(obj, find, replace):
    if type(obj) == str:
        return obj.replace(find, replace)
    return [replace if o == find else o for o in obj]