class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1 + nums2
        merged.sort()
        ret = 0.0
        median = merged[(len(merged) / 2)]
        median2 = merged[(len(merged) / 2) - 1]
        if len(merged) % 2 == 0:
            print(median + median2)
            ret += (float(median + median2) / 2)
        else:
            ret = median
        return ret
