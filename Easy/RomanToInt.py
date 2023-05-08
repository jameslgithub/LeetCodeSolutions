class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0
        while (i < len(s)):
            cur1 = roman[s[i]]
            if i + 1 < len(s):
                cur2 = roman[s[i + 1]]
                if cur1 >= cur2:
                    total = total + cur1
                    i += 1
                else:
                    total = total - cur1
                    i += 1
            else:
                total = total + cur1
                i += 1

        return total
