class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        ret = 0
        for i in range(len(accounts) ):
            sum1 = 0
            for j in range(len(accounts[i])):
                sum1 += accounts[i][j]
            if ret < sum1:
                ret = sum1
        return ret
