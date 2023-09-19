class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ret = ''
        for i in range(len(command)):
            if command[i] == '(' and command[i + 1] == ')':
                ret += 'o'
            elif command[i] == '(' and command[i + 1] != ')':
                ret += 'al'
            elif command[i] == 'G':
                ret += 'G'

        return ret
        
