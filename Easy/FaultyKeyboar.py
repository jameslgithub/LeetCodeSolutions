class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        for i in s:
            if i == 'i':
                ret = ret[::-1]
            else:
                ret += i

        return ret
