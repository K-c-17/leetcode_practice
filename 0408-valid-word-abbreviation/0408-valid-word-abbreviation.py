class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i,j=0,0

        while i<len(word) and j<len(abbr):
            
            #if an alphabet
            if abbr[j].isalpha():
                if word[i]!=abbr[j]:
                    # print("first")
                    return False
                else:
                    i+=1
                    j+=1
            
            #not an alphabet
            elif abbr[j]=='0':
                # print("second")
                return False
            
            elif abbr[j].isdigit():
                num=''
                while j<len(abbr) and abbr[j].isdigit():
                    num+=abbr[j]
                    j+=1
                i+=int(num)
        
        # print("third")    
        return (i==len(word)) and (j==len(abbr))
            
