class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code_list=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    
        alpha_code_map={alpha_list[i]:code_list[i] for i in range(len(alpha_list))}
        
        start=''
        collector=[]
        for val in words:
            for alp in val:
                start+=alpha_code_map[alp]
            if start not in collector:
                collector.append(start)
            start=''
        return len(collector)