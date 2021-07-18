class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = set(brokenLetters)
        return len([1 for word in text.split() if len(set(word).intersection(s)) == 0 ])
        
