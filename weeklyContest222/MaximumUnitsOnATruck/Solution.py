class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        n = len(boxTypes)
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        r = truckSize
        i = 0
        res = 0
        while i < n and r > 0:
            if boxTypes[i][0] <= r:
                res += boxTypes[i][0] * boxTypes[i][1]
                r -= boxTypes[i][0]
            else:
                res += r * boxTypes[i][1]
                break
            i+=1
        return res
    