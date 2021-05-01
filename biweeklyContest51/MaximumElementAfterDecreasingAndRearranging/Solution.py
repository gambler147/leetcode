class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # sort and greedy, O(nlogn)
        arr.sort()
        # set arr[0] = 1
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i-1] + 1, arr[i])
        return arr[-1]
    