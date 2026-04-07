class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        def backtrack(start, path, remaining, k):
            
            if len(path) == k and remaining == 0:
                res.append(path[:])
            
            for i in range(start, 9):
                if numbers[i] > remaining:
                    break
                path.append(numbers[i])
                backtrack(i + 1, path, remaining - numbers[i], k)
                path.pop()
        backtrack(0, [], n, k)
        return res