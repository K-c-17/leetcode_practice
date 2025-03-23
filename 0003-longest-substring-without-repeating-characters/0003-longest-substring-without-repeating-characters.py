class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        elif s.strip()=='' and len(s)>=1:
            return 1
        elif len(s)==1:
            return 1

        l,r,max_len=0,1,0

        while r<len(s):
            match=False
            for i in range(l,r):
                if s[i]==s[r]:
                    match=True
                    max_len=max(max_len,r-l)
                    l=i+1
                    break
            
            if not match and r==len(s)-1:
                max_len=max(max_len,r-l+1)
                break
            elif not match:
                r+=1
            print(max_len)
        
        return max_len
                

                






        
            


        