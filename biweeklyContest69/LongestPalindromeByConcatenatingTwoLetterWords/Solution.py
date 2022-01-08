class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # using counters
        word_cnt = collections.Counter(words)
        word_set = set(words)
        
        l = 0
        # iterate the word_set
        for w in word_set:
            if word_cnt[w] <= 0:
                continue
                
            rw = w[::-1]
            if word_cnt[rw] <= 0:
                continue
            
            # check if w == rw
            if w == rw and word_cnt[rw] > 1:
                d = word_cnt[w]//2
                word_cnt[w] -= 2*d
                l += 4*d
            elif w != rw:
                d = min(word_cnt[w], word_cnt[rw])
                word_cnt[w] -= d
                word_cnt[rw] -= d
                l += 4*d
                
        # check for middle pair
        for w in word_set:
            if w == w[::-1] and word_cnt[w] > 0:
                l += 2
                break
        
        return l
    
