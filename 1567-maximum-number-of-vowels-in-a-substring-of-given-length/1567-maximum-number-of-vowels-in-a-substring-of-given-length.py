class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start,end=0,k
        vowels={'a', 'e', 'i', 'o', 'u'}
        
        comp_size=sum(1 for char in s[start:end] if char in vowels)
        max_size=comp_size
        while end<=len(s)-1:
            
            if s[start] in vowels and s[end] not in vowels:
                comp_size-=1
            elif s[start] not in vowels and s[end] in vowels:
                comp_size+=1
            
            if comp_size>max_size:
                max_size=comp_size
            
            start+=1
            end+=1

        return max_size