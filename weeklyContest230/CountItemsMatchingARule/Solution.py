class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        m = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        for l in items:
            if l[m[ruleKey]] == ruleValue:
                res += 1
        return res
            