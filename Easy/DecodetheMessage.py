class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        dec = {' ': ' '}
        count = 0
        ret = ''
        for i in key:
            if i not in dec:
                dec[i] = letters[count]
                count += 1
        for i in message:
            ret += dec[i]
        
        print(ret)
        return ret
