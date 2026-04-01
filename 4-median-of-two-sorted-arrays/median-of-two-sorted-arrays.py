class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        new = nums1 + nums2
        new.sort()
        left = 0
        right = len(new)-1
        while left < right:
            left += 1
            right -= 1
        return ((new[left] + new[right])/ 2)