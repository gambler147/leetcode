class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # count 0s and 1s for students,
        # loop the sandwiches until no students remaining wants the first sandwich
        sc = collections.Counter(students)
        remaining = len(sandwiches)
        for s in sandwiches:
            if sc[s] <= 0:
                return remaining
            else:
                sc[s] -= 1
                remaining -= 1
        return 0
    