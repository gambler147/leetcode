class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        import re
        word = re.sub("[a-z]+", " ", word).split()
        return len(set(int(w) for w in word))
    