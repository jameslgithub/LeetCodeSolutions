class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = {}
        retval = 0
        for i in nums:
            if i in temp:
                temp[i] = False
            else:
                temp[i] = True
        
        for i in temp:
            if temp[i]:
                retval = i
        return retval
        

        
