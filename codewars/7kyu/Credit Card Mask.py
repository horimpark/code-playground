def maskify(cc):
    if len(cc) < 4:
        return cc
    answer = "#" * len(cc[:-4])
    answer += cc[-4:]

    return answer


if __name__ == "__main__":
    print(maskify("4556364607935616"))  # ############5616
    print(maskify("64607935616"))  # #######5616
    print(maskify("1"))  # 1
    print(maskify(""))  # ""
    print(maskify("Skippy"))  # ##ippy
    print(maskify("Nananananananananananananananana Batman!"))  # ####################################man!