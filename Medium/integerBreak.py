class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n<=3): 
            return n-1
        elif (n % 3) == 0:
            return 3**(n/3)
        elif (n % 3) == 1:
            return 3**(n/3 - 1)*4
        else:
            return 3**(n/3)*2
