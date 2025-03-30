class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def longestPalindromeHelper(s, t, right=False):
            sList = []
            SEP = "#"
            for char in s:
                sList.append(char)
                sList.append(SEP)
    
            # construct t substring map
            tSet = set()
            n = len(t)
            for i in range(n):
                for j in range(i, n):
                    tSet.add(t[i:j+1][::-1])
    
            res = 0
            # now for each element in s as the center of Palindrome, check max length
            for center in range(len(sList)):
                # find max palidrome from s
                l, r = center, center
                count = 0
                while l >= 0 and r < len(sList) and sList[l] == sList[r]:
                    if sList[l] != SEP:
                        count += 1 + (l != r)
                    l -= 1
                    r += 1

                res = max(res, count)
                # check substring before sList[l] and if anything in t
                temp = ""
                [start, end, dir] = [r, len(sList), 1] if right else [l, -1, -1]
                for ll in range(start, end, dir):
                    if sList[ll] != SEP:
                        temp = temp + sList[ll] if right else sList[ll] + temp
                        if temp in tSet:
                            res = max(res, count + 2*len(temp))
                        else:
                            break
    
            return res

        return max(longestPalindromeHelper(s, t), longestPalindromeHelper(t, s, right=True))
