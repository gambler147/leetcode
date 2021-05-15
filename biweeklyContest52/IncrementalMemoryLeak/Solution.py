class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        # find n such that 1 + .. + n > memory1 + memory2
        i = 1
        while max(memory1, memory2) >= i:
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i+=1
        return [i, memory1, memory2]
    