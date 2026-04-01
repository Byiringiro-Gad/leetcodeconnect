class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        while low <= high:
            partitionx = (low+high)//2
            partitiony = (x+y+1)//2 - partitionx

            max_leftx = float("-inf") if partitionx == 0 else nums1[partitionx-1]
            min_rightx = float("inf") if partitionx == x else nums1[partitionx]
            
            max_lefty = float("-inf") if partitiony == 0 else nums2[partitiony-1]
            min_righty = float("inf") if partitiony == y else nums2[partitiony]
            
            if max_leftx <= min_righty and max_lefty <= min_rightx:
                if (x+y) % 2 == 0:
                    return (max(max_leftx, max_lefty) + min(min_righty, min_rightx))/2
                else:
                    return max(max_leftx, max_lefty)
            elif max_leftx > min_righty:
                high = partitionx - 1
            else:
                low = partitionx + 1