class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res,  sol = [], []
        nums.sort()
        def dfs(i):
            if i == len(nums):
                res.append(sol[:])
                return
            dfs(i+1)
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
        dfs(0)
        new = []
        for n in res:
            if n not in new:
                new.append(n)
        return new



