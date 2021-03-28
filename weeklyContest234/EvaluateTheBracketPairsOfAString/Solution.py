class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        kldg = {k: v for k,v in knowledge}
        stack = []
        cur = []
        for c in s:
            if c == '(':
                # start of a key
                s = ''.join(cur)
                stack.append(s)
                cur = []
            elif c == ')':
                # cur is a key and find its value in knowledge
                s = ''.join(cur)
                if s in kldg:
                    stack.append(kldg[s])
                else:
                    stack.append("?")
                cur = []
            else:
                cur.append(c)
        
        if cur:
            stack.append(''.join(cur))
        
        return ''.join(stack)
                