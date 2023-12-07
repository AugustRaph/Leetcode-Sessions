class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        output=""
        temp=""
        for i in num:
            temp+=i
            if int(i)%2==1:
                output=temp
        return output        