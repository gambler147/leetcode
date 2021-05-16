class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # counter for nums2
        self.arr1 = nums1
        self.arr2 = nums2
        self.cnt2 = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        prev = self.arr2[index]
        self.cnt2[prev] -= 1
        self.arr2[index] += val
        self.cnt2[self.arr2[index]] += 1
        
    def count(self, tot: int) -> int:
        res = 0
        for v in self.arr1:
            res += self.cnt2[tot - v]
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)