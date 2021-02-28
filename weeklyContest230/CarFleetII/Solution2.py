class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # monotonic stack; we only care about time for each car to collide with next car
        n = len(cars)
        res = [-1 for _ in range(n)]
        # we maintain a stack with cars' collision time strictly increasing
        stack = []
        for i in range(n-1,-1,-1):
            p, s = cars[i]
            # we check if current car is slower than cars in the stack, if so, we pop from stack 
            # until the car's speed is faster
            while stack and (s <= cars[stack[-1]][1] or 
                             (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1]) >= res[stack[-1]] and res[stack[-1]] != -1):
                stack.pop()
            # if there is a car in the stack slower than current car, we update current car's collision time
            if stack:
                res[i] = (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1])
            stack.append(i)
        return res
            
            