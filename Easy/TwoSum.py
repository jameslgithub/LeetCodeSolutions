class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nlen = len(nums)
        ret = list()
        for i in range(0, nlen-1):
            ttemp = 0
            for x in range(i + 1, nlen):
                if ((nums[i] + nums[x]) == target):
                    ret.append(i)
                    ret.append(x)
        return ret
