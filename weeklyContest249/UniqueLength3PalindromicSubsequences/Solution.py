class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # reference:
        # https://leetcode.com/problems/unique-length-3-palindromic-subsequences/discuss/1330178/Python-Straight-Forward-Solution
        
        # for each character, find its first occurrence and last occurence in the string
        # and count distinct characters in between
        # time O(26n) space O(26)
        res = 0
        for c in range(26):
            l, r = s.find(c), s.rfind(c)
            if l > -1:
                res += len(set(s[l+1:r]))
        return res
    
        
    
