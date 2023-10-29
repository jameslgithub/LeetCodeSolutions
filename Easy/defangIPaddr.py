class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ret = ''

        for i in address:
            if i == '.':
                ret += '[.]'
            else:
                ret += i
        return ret
        
