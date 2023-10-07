class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rep = set()
        count = 0
        tot = 0
        for i in range(len(s)):
            if s[i] not in rep:
                rep.add(s[i])
                tot = max(tot, i - count + 1)
            else: 
                while s[i] in rep:
                    rep.remove(s[count])
                    count += 1
                rep.add(s[i])
        return tot
