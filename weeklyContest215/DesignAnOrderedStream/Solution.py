class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None] * 1001
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        res = []
        self.arr[id] = value
        if (id == self.ptr):
            ptr = id
            while self.arr[ptr] != None:
                res.append(self.arr[ptr])
                ptr += 1
            self.ptr = ptr
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
