class CaesarCipher(object):
    def __init__(self, shift):
        self.alphabet = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
        self.shift = shift

    def encode(self, st):
        result = ""
        for x in st:
            if not x.isalpha():
                result += x
                continue
            x = x.upper()
            new_idx = self.alphabet.index(x) + self.shift
            if new_idx >= 26:
                result += self.alphabet[new_idx - 26]
            else:
                result += self.alphabet[new_idx]
        return result

    def decode(self, st):
        result = ""
        for x in st:
            if not x.isalpha():
                result += x
                continue
            x = x.upper()
            new_idx = self.alphabet.index(x) - self.shift
            if new_idx < 0:
                result += self.alphabet[new_idx + 26]
            else:
                result += self.alphabet[new_idx]
        return result


# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
