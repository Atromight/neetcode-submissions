
LETTER_ORDER = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}


class PrefixTree:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


    def insert(self, word: str) -> None:
        curr = None
        if word:
            letter = word[0]
            word = word[1:]
            # Letter doesn't exist in children
            if not self.children[LETTER_ORDER[letter]]:
                self.children[LETTER_ORDER[letter]] = PrefixTree()

            curr = self.children[LETTER_ORDER[letter]]
            curr.insert(word)

        else: # not word
            self.isEndOfWord = True


    def search(self, word: str) -> bool:
        if word:
            letter = word[0]
            word = word[1:]
            if not self.children[LETTER_ORDER[letter]]:
                return False

            curr = self.children[LETTER_ORDER[letter]]
            return curr.search(word)

        else: # not word
            if self.isEndOfWord == True:
                return True
            else:
                return False


    def startsWith(self, prefix: str) -> bool:
        if prefix:
            letter = prefix[0]
            prefix = prefix[1:]
            if not self.children[LETTER_ORDER[letter]]:
                return False

            curr = self.children[LETTER_ORDER[letter]]
            return curr.startsWith(prefix)

        else: # not prefix
            return True


        
        