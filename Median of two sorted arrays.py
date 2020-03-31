"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_nums = nums1+nums2
        total_nums.sort()
        len_total = len(total_nums)
        if len_total%2!=0:
            return total_nums[len_total//2]
        else:
            midpoint = len_total//2
            return 0.5*(total_nums[midpoint-1]+total_nums[midpoint])
