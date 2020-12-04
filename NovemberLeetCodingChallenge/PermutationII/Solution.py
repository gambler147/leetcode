class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:        
        res = [[]] # initially with empty

        for num in nums:
            new_res = []
            # we add number to current results one by one
            for l in res:
                # iterate each current list from result
                for i in range(len(l) + 1):
                    # len(l) + 1 spots we can insert new value
                    new_res.append(l[:i] + [num] + l[i:])
                    # notice that if we have reached to index i that l[i] == num
                    # we stop the iteration since further cases will be covered
                    # in other lists in l. e.g. if we have
                    # res = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
                    # when we want to insert 1 to [2,1,3]
                    # we create [1,2,1,3], [2,1,1,3] then we stop 
                    # since if we insert to third position we will have [2,1,1,3] which is duplicate
                    # and if we insert into fourth position we will have [2,1,3,1] which is duplicate
                    # when you insert 1 to [2,3,1] in second position
                    if i < len(l) and l[i] == num:
                        break
            res = new_res
        
        return res
