class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping=Counter(s)

        total,is_odd=0,False

        for i in mapping.values():
            total+=(i//2)*2
            if i%2 == 1:
                is_odd=True
        
        if is_odd:
            total+=1
        
        return total
        