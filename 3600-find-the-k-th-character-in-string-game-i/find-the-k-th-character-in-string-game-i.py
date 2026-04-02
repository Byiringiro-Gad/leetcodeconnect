class Solution:
    def kthCharacter(self, k: int) -> str:
        def helper(k):
            if k == 1:
                return 0
            length = 1
            while length < k:
                length *= 2
            half = length//2
            if k <= half:
                return helper(k)
            else:
                return helper(k - half) + 1
        val = helper(k) % 26
        return chr(ord("a") + val)