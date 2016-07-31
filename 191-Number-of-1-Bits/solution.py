class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
            
        i=0
        count=0
        while i<32:
            if n&1:
                count+=1
            n=n>>1
            i+=1
        return count