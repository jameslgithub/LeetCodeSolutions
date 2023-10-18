class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        isdiv = 0
        nondiv = 0
        for i in range(1,n + 1):
            if i % m == 0:
                isdiv += i
            else:
                nondiv += i
         
        return nondiv - isdiv
        
