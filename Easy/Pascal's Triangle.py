class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        retVal=[]
        retVal.append([1]) 
        for i in range(numRows-1):
            temp=[1]
            for j in range(i): # range: 0 = []; 1 = [0]; 2 = [0, 1] 
                temp.append(retVal[i][j]+retVal[i][j+1]) 
            temp.append(1)
            retVal.append(temp)
        return retVal
                        
