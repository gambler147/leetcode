class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # minium k numbers in the array use stack?
        n = len(nums)
        stack = []
        for i, num in enumerate(nums):
            while stack and num < stack[-1] and n-i > k - len(stack):
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack