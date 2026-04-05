class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        
        def backtrack(start, remaining, path):
            if len(path) == k and remaining == 0:
                res.append(path[:])
                return
            
            if len(path) > k or remaining < 0:
                return
            
            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1, remaining - num, path)
                path.pop()
        
        backtrack(1, n, [])
        return res