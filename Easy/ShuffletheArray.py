class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ret = []
        for i in range(0, len(nums) / 2):
            ret.append(nums[i])
            ret.append(nums[i + n])
        return ret
        
