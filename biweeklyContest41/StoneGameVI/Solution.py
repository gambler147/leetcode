class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        nets = []
        for av, bv in zip(aliceValues, bobValues):
            nets.append(av+bv)
            
        nets = sorted([(v, i) for i,v in enumerate(nets)], reverse=True)
        net_score = 0
        for k, (v, i) in enumerate(nets):
            net_score += aliceValues[i] if (k%2==0) else -bobValues[i]
        
        if net_score == 0: res = 0
        elif net_score > 0: res = 1
        else: res = -1
        return res