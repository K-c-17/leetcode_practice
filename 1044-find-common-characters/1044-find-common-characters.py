class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        collector=[]
        for value in words:
            sample=dict.fromkeys(string.ascii_lowercase,0)
            for alpha in value:
                sample[alpha]+=1
            collector.append(sample)
        
        min_dict={}
        
        for dic_val in collector:
            for i in dic_val:
                if i not in min_dict or min_dict[i]>dic_val[i]:
                    min_dict[i]=dic_val[i]
                else:
                    pass

        result=[]
        for j in min_dict:
            for k in range(min_dict[j]):
                result.append(j)
        
        return result
            
                    
                
            
            
            
        