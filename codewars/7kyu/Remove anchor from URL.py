def remove_url_anchor(url):
    test = url.find("#")
    return url[:test] if test != -1 else url
