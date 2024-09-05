def DNA_strand(dna):
    return dna.translate(str.maketrans('ATCG', 'TAGC'))


if __name__ == "__main__":
    print(DNA_strand("ATTGC"))  # "TAACG"
    print(DNA_strand("GTAT"))  # "CATA"
    print(DNA_strand("AAGG"))  # "TTCC"
    print(DNA_strand("CGCG"))  # "GCGC"
    print(DNA_strand("ATAT"))  # "TATA"
    print(DNA_strand("CGGC"))  # "GCCG"
    print(DNA_strand("ATCG"))  # "TAGC"
    print(DNA_strand("ATGC"))  # "TACG