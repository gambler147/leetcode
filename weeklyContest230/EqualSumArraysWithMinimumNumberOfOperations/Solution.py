class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # greedy; find sums of nums1 and nums2, say sum(nums1) < sum(nums2)
        # then change either smallest element in nums1 to 6 or biggest element in nums2 to 1
        cnt1 = collections.Counter(nums1)
        cnt2 = collections.Counter(nums2)
        
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 > s2:
            # switch
            cnt1, cnt2, s1, s2 = cnt2, cnt1, s2, s1
        
        ops = 0
        while s1 < s2:
            for v in range(1, 6):
                if cnt1[v] > 0:
                    if 6-v >= s2 - s1:
                        # if 6 - v >= s2 - s1, then we can finish in this operation
                        ops += 1
                        return ops
                    else:
                        # other wise we increase as much as we can
                        ops += 1
                        cnt1[v] -= 1
                        cnt1[6] += 1
                        s1 += 6-v
                    break
                        
                elif cnt2[7-v] > 0:
                    if 6-v >= s2 - s1:
                        ops += 1
                        return ops
                    else:
                        ops += 1
                        cnt2[7-v] -= 1
                        cnt2[1] += 1
                        s2 -= (6-v)
                    break
            # if not update in this loop, return -1
            else:
                return -1

        return ops
                        