class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        tasks.sort(key = lambda x: x[0] - x[1])
        energy = 0
        cost = 0
        for i in range(n):
            if energy < tasks[i][1]:
                cost += tasks[i][1] - energy
                energy = tasks[i][1]
            energy -= tasks[i][0]
        return cost