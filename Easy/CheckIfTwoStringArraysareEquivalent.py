class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        wordone = ''.join(word1)
        wordtwo = ''.join(word2)
        if wordone == wordtwo:
            return True
        else:
            return False
    
