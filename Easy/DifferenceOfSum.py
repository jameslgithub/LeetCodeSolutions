class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = sum(nums)
        tot2 = ''
        dig = 0
        for i in (nums):
            if i > 9:
                tot2 += str(i)
            else:
                tot2 += str(i)
        for i in tot2:
            dig += int(i)
        
        return abs(tot - dig)
        
