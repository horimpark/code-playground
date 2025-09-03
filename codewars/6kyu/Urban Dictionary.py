class WordDictionary:
    def __init__(self):
        self.word_dict = list()

    def add_word(self, word):
        self.word_dict.append(word)

    def search(self, word):
        print(word)
        split_word = [x for x in word]
        candidates = [x for x in self.word_dict if len(x) == len(word)]
        for cand in candidates:
            res = [s==cand[i]  for i, s in enumerate(split_word) if s!='.']
            if all(res):
                return True
        else:
            return False
