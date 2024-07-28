def domain_name(url):
    url = "".join(url.split("://")[-1]).split(".")
    if url[0] == "www":
        return url[1]
    else:
        return url[0]
