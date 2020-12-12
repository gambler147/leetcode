class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for word in words:
            if len(set(word) - allowed) == 0:
                res += 1
        return res