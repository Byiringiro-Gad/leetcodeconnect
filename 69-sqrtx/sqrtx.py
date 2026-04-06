class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        ans = 0
        left, right = 0, x//2
        while left <= right:
            mid = (left + right)// 2
            if mid * mid ==  x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
                ans = mid
        return ans
