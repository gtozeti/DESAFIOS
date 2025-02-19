# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = list()
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if len(nums1) > 0 and len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (
                    nums1[int(len(nums1) / 2)] + nums1[int((len(nums1) / 2) - 1)]
                ) / 2
            return nums1[int(((len(nums1) + 1) / 2) - 1)]
        if len(nums2) > 0 and len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (
                    nums2[int(len(nums2) / 2)] + nums2[int((len(nums2) / 2) - 1)]
                ) / 2
            return nums2[int(((len(nums2) + 1) / 2) - 1)]
        merged_array.extend(nums1)
        merged_array.extend(nums2)
        merged_array.sort()
        if len(merged_array) % 2 == 0:
            return (
                merged_array[int(len(merged_array) / 2)]
                + merged_array[int((len(merged_array) / 2) - 1)]
            ) / 2
        return merged_array[int(((len(merged_array) + 1) / 2) - 1)]

s = Solution()
s.findMedianSortedArrays([1,2],[3,4,5])
