class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        cur = first
        for num in encoded:
            cur ^= num
            res.append(cur)
        return res
    