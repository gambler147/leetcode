class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        # the greedy algo is not working
        # use dfs with memorization. 
        # we first calculate the remainder of each group with respect to batchSize
        # use a list to count the remainders. 
        self.batchSize = batchSize
        cnt = [0 for _ in range(batchSize)] # count of modulus
        
        for g in groups:
            cnt[g%batchSize] += 1
        
        res = cnt[0]
        # clear modulo 0
        cnt[0] = 0
        self.memo = {}
        
        res += self.dfs(cnt, 0)
        return res
        
        
    def dfs(self, cnt, mod):
        # return the maximum possible happy groups (cnt) with current modulo is mod
        # we stop if cnt is empty
        for i in range(self.batchSize):
            if cnt[i] != 0:
                break
        else:
            return 0
        
        # turn cnt to a string as key in memo
        key = ''.join(list(map(str,cnt))) + str(mod)
        
        if key in self.memo:
            return self.memo[key]
        
        # if current modulo is 0 then the current group is happy otherwise not
        cur = 1 if mod == 0 else 0
        
        happy = 0
        for i in range(1, self.batchSize):
            if cnt[i] > 0:
                cnt[i]-=1
                happy = max(happy, self.dfs(cnt, (mod+i) % self.batchSize))
                cnt[i] += 1
        
        # put result to memo
        self.memo[key] = cur + happy
        
        return self.memo[key]
        
        