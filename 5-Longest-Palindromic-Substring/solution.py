class Solution(object):
    def longestPalindromeDP(self,s):
        """
        define: dp[i][j] means whether subtring[i,j] is a palindrome
        initial: dp[i][i] is true, for the single char
                dp[i][i+1] is true if s[i]==s[i+1]
        dp[i][j]=dp[i+1][j-1] if s[i]==s[j]
        """
        n=len(s)
        maxstart,maxlen=0,1
        dp=[[False for _ in xrange(n)] for _ in xrange(n)]
        
        for i in xrange(n):
            dp[i][i]=True
        for i in xrange(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                maxstart=i
                maxlen=2
        
        for k in xrange(3,n+1):
            # keep the length of palindrom is k, so i stop at n-k+1
            for i in xrange(n-k+1):
                # for padlinrome length of k, j start at i+k-1
                j=i+k-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    maxstart=i
                    maxlen=k
        return s[maxstart:maxstart+maxlen]
            
                
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.longestPalindromeDP(s)
        
        if not s:
            return ""
        str_len=len(s)
        longest=s[0]
        for i in range(str_len-1):
            p1=self.expandfromcenter(s,i,i)
            if len(p1)>len(longest):
                longest=p1
                
            p2=self.expandfromcenter(s,i,i+1)
            if len(p2)>len(longest):
                longest=p2
                
        return longest
    
    def expandfromcenter(self,s,c1,c2):
        left=c1
        right=c2
        str_len=len(s)
        while left>=0 and right<=str_len-1 and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    

    
    
    