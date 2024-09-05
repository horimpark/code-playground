def DNA_starnd(dna):
    return dna.translate(str.maketrans('ATCG', 'TAGC'))


if __name__ == "__main__":
    print(DNA_starnd("ATTGC"))  # "TAACG"
    print(DNA_starnd("GTAT"))  # "CATA"
    print(DNA_starnd("AAGG"))  # "TTCC"
    print(DNA_starnd("CGCG"))  # "GCGC"
    print(DNA_starnd("ATAT"))  # "TATA"
    print(DNA_starnd("CGGC"))  # "GCCG"
    print(DNA_starnd("ATCG"))  # "TAGC"
    print(DNA_starnd("ATGC"))  # "TACG