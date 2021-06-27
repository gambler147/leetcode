class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # bitmask and prefix counter
        
        # for each letter, to find number of substrings ending at current letter, use a bitmask where each bit
        # represents the parity of the ith letter in the substring. We use a counter to count all the prefix substrings'
        # bitmasks. A substring bitmask is wonderful if and only if the bitmask has 1 in at most 1 bit. 
        # So, for each letter, to find how many substrings ending at current letter are wonderful, we count how many
        # bitmasks occurred before that has at most 1 bit different with current prefix substring bitmask. 
        # time O(dn), space O(2^d), here d = 10 is distinct letters
        
        counter = collections.Counter({0: 1})
        cur = 0
        res = 0
        for w in word:
            cur ^= 1 << (ord(w) - ord('a'))
            res += counter[cur]
            for k in range(10):
                res += counter[cur ^ (1 << k)]
            counter[cur] += 1
        return res
    