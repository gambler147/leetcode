class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        # Same as longest non-decreasing array.
        # Space : O(1); Time: O(n)
        n = len(word)
        cur = 0 # current length of substring
        res = 0 # longest length of substring
        cur_set = set()
        for i in range(n):
            if cur > 0 and word[i] < word[i-1]:
                # if current char is smaller than previous one, we start over our substring
                cur = 1
                cur_set = set([word[i]])
            else:
                # if current char is greater or equal than previous one, the substring can be extended
                cur += 1
                cur_set.add(word[i])
            # we update the result if and only if 5 vowels are present in the set
            if len(cur_set) == 5:
                res = max(res, cur)
        return res
                