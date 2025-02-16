class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # greedy
        n = len(pizzas)
        days = n // 4
        odd_days = (days + 1) // 2
        even_days = days - odd_days
        # you can eat odd days for biggest pizzas first
        pizzas.sort()
        total_weight = 0
        for i in range(odd_days):
            total_weight += pizzas.pop()

        for i in range(1, even_days+1):
            total_weight += pizzas[-i*2]

        return total_weight

