import re

regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$"


def search(regex, string):
    return re.search(regex, string)
