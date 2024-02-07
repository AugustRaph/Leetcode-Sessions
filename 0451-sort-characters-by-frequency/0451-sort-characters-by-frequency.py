class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        k={}
        for i in s:
            if i in k:
                k[i]+=1
            else:
                k[i]=1
        k=sorted(k.items(), key=lambda x:x[1],reverse=True)
        r=''
        for i,v in k:    
            r=r+i*v
        return r