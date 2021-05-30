class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        getVal = lambda word: int(''.join([str(ord(c) - ord('a')) for c in word]))
        return getVal(firstWord) + getVal(secondWord) == getVal(targetWord)
                