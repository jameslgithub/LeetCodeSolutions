class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ret = ""
        for i in range(len(indices)):
            ret += s[indices.index(i)]

        return ret
