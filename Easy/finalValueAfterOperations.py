class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        tot = 0
        for i in operations:
            if i == "--X" or i == "X--":
                tot -= 1
            else:
                tot += 1
        return tot
