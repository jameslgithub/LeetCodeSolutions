class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        temp = s.split(' ')
        for i in temp:
            ret += i[:: -1]
            ret += ' '
        return ret[: -1]
        
