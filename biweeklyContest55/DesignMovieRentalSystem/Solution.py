class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        # use one sorted list to maintain the rented movies (shop, movie) 
        # and dictionary of sortedlists to maintain unrented movies movid_i: (price_j, shop_j)
        # use additional dictionary to map the (shop, movie) -> price
        # when rent a movie, remove item from unrented and insert to rented. This takes O(logn)
        # when drop a movie, remove item from rented and insert to unrented. This takes O(logn)
        # for search and report. It takes O(logn)
        # time: O(nlogn + qlog(n)) space O(nlogn), n is the entries size and q is the query size
        
        from sortedcontainers import SortedList
        from collections import defaultdict
        # entries sorted by [price, shop, movie]
        self.pricemap = dict()
        self.unrented = collections.defaultdict(SortedList)
        self.rented = SortedList()
        for shop, movie, price in entries:
            self.pricemap[(shop, movie)] = price
            self.unrented[movie].add([price, shop])
        

    def search(self, movie: int) -> List[int]:
        # O(logn)
        # return first 5 elements from self.unrented
        top5 = self.unrented[movie][:5]
        return [shop for (price, shop) in top5]

    def rent(self, shop: int, movie: int) -> None:
        # O(logn)
        # remove element from self.entries, self.unrented
        price = self.pricemap[(shop, movie)]
        self.unrented[movie].remove([price, shop])
        self.rented.add([price, shop, movie])
        

    def drop(self, shop: int, movie: int) -> None:
        # O(logn)
        # add elemetn to self.entries, self.unrented
        price = self.pricemap[(shop, movie)]
        self.unrented[movie].add([price, shop])
        self.rented.remove([price, shop, movie])
        
    def report(self) -> List[List[int]]:
        # O(logn)
        top5 = self.rented[:5]
        return [[shop, movie] for (price, shop, movie) in top5]
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()