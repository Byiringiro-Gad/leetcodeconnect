class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max1 = float("-inf")
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] == colors[j]:
                    continue
                else:
                    max1 = max(max1, abs(i-j))
        return max1