class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        ret = []
        ret2 = []
        
        for i in range(len(heights)):
            ret.append([heights[i],names[i]])
        ret = sorted(ret, reverse = True)

        for i in ret:
            ret2.append(i[1])
        
        return ret2
