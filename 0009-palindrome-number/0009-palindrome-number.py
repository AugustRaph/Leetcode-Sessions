class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)[::-1]
        if y == str(x):
            return True
        else:
            return False
