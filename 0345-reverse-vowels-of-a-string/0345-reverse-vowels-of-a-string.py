class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        first=0
        last=len(s)-1
        s=list(s)
        while first<last:
            if s[first].lower() in 'aeiou' and s[last].lower() in 'aeiou':
                s[first],s[last]=s[last],s[first]
                first+=1
                last-=1
            elif s[first].lower() not in 'aeiou' and s[last].lower() not in 'aeiou':
                first+=1
                last-=1
            elif s[first].lower() not in 'aeiou':
                first+=1
            elif s[last].lower() not in 'aeiou':
                last-=1
        return ''.join(s)
