class Solution(object):
    def isPalindrome(self, x):
        if (str(x)[::-1]) == str(x):
            return True
        False
        """
        :type x: int
        :rtype: bool
        """
