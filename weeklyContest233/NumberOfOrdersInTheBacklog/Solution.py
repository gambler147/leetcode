class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # use two heaps
        buy_h = [] # element (-price, amount)
        sell_h = [] # element (price, amount)
        for price, amount, orderType in orders:
            if orderType == 0:
                heapq.heappush(buy_h, (-price, amount))
            else:
                heapq.heappush(sell_h, (price, amount))
            # check if order can be executed
            while buy_h and sell_h and -buy_h[0][0] >= sell_h[0][0]:
                best_buy = heapq.heappop(buy_h)
                best_sell = heapq.heappop(sell_h)
                fill = min(best_buy[1], best_sell[1])
                if best_buy[1] - fill > 0:
                    heapq.heappush(buy_h, (best_buy[0], best_buy[1]-fill))
                if best_sell[1] - fill > 0:
                    heapq.heappush(sell_h, (best_sell[0], best_sell[1]-fill))
                    
        # return total number of order in both heaps
        res = 0
        for _, amount in buy_h:
            res += amount
        for _, amount in sell_h:
            res += amount
        return res % (10**9+7)
    