class Bitset:
    # Use a boolean flag to denote parity of flips and we do not need to modify the bits array
    # O(1) for fix, unfix, flip, all and count
    # O(size) for toString
    def __init__(self, size: int):
        self.flipped = 0
        self.size = size
        self.sum = 0 # count of ones
        self.bits = [0 for _ in range(size)]

    def fix(self, idx: int) -> None:
        if not (self.flipped ^ self.bits[idx]):
            self.sum += 1
        self.bits[idx] = 1-self.flipped

    def unfix(self, idx: int) -> None:
        if self.flipped ^ self.bits[idx]:
            self.sum -= 1
        self.bits[idx] = self.flipped

    def flip(self) -> None:
        self.flipped = 1-self.flipped
        self.sum = self.size - self.sum

    def all(self) -> bool:
        return self.sum == self.size

    def one(self) -> bool:
        return self.sum >= 1

    def count(self) -> int:
        return self.sum        

    def toString(self) -> str:
        return "".join([str(self.bits[i]^self.flipped) for i in range(self.size)])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()