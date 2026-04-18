class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(num * num)
        return sorted(ans)    
        