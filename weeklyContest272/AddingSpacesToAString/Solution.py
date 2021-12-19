class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        stack = []
        j = 0
        for i in range(n):
            if j < len(spaces) and i == spaces[j]:
                stack.append(" ")
                j += 1
            stack.append(s[i])
        return ''.join(stack)
            
