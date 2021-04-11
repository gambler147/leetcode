from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.size = 0
        self.m = m
        self.k = k
        self.arr = []
        self.mid_tree_sum = 0 # sum of mid_tree
        # use 3 self balanced binary search tree
        self.max_tree = SortedList()
        self.min_tree = SortedList()
        self.mid_tree = SortedList()
        
    def addElement(self, num: int) -> None:
        self.arr.append(num)
        self.size += 1
        if self.size < self.m:
            return
        
        if self.size == self.m: 
            # initialize tree
            arr = sorted(self.arr)
            self.min_tree.update(arr[:self.k])
            self.mid_tree.update(arr[self.k:(self.m-self.k)])
            self.mid_tree_sum += sum(arr[self.k:(self.m-self.k)])
            self.max_tree.update(arr[(self.m-self.k):self.m])
            return
        
        # if trees are initialized, we need to pop out value at self.arr[self.size-1-k]
        last = self.arr[self.size-1-self.m]
        # determine which tree this value belongs to
        # 1. if last is bigger or equal than min_val in mid_tree and less or equal than max_val in mid_tree, pop from mid_tree
        # 2. if last is bigger than max_val in mid_tree, pop from max_tree
        # 3. if last is less than min_val in mid_tree, pop from min_tree
        mid_min = self.mid_tree[0]
        mid_max = self.mid_tree[-1]
        if mid_min <= last <= mid_max:
            self.mid_tree.remove(last)
            self.mid_tree_sum -= last
        
        elif last > mid_max:
            self.max_tree.remove(last)
        
        else:
            self.min_tree.remove(last)
            
        # now we make max_tree and min_tree size of k
        if len(self.max_tree) < self.k:
            val = self.mid_tree.pop(-1)
            self.mid_tree_sum -= val
            self.max_tree.add(val)
        
        if len(self.min_tree) < self.k:
            val = self.mid_tree.pop(0)
            self.mid_tree_sum -= val
            self.min_tree.add(val)
            
        # now we try insert new num to trees
        # check insert into max_tree
        if num > self.max_tree[0]:
            self.max_tree.add(num)
            num = self.max_tree.pop(0)
        
        # check insert into min_tree
        if num < self.min_tree[-1]:
            self.min_tree.add(num)
            num = self.min_tree.pop(-1)
        
        # insert into mid_tree
        self.mid_tree.add(num)
        self.mid_tree_sum += num
        

    def calculateMKAverage(self) -> int:
        if self.size < self.m:
            return -1
        
        return self.mid_tree_sum // (self.m - 2*self.k)
        
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()