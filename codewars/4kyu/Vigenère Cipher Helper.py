class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key_map = [(x, self.alphabet.index(x)) for x in key]

    def transfer(self, text, is_encode):
        print(text)
        encoded = ""
        key_map = (self.key_map * ((len(text) // len(self.key_map)) + 1))[: len(text)]
        for t, k in zip(text, key_map):
            if t in self.alphabet:
                if is_encode is True:
                    ec_idx = self.alphabet.index(t) + k[1]
                    if ec_idx > len(self.alphabet) - 1:
                        ec_idx = ec_idx - len(self.alphabet)
                    encoded += self.alphabet[ec_idx]
                else:
                    ec_idx = self.alphabet.index(t) - k[1]
                    if ec_idx < 0:
                        ec_idx = len(self.alphabet) + ec_idx
                    encoded += self.alphabet[ec_idx]
            else:
                encoded += t
        return encoded

    def encode(self, text):
        encoded = self.transfer(text, is_encode=True)
        return encoded

    def decode(self, text):
        decoded = self.transfer(text, is_encode=False)
        return decoded
