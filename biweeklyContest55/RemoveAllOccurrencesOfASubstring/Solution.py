class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # brute force
        # time O(nm) space O(1), where n is size of s and m is size of part
        while s.find(part) != -1:
            s = s.replace(part, '')
        return s
            