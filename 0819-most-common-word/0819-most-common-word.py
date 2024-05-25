class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        collector={}
        new_para=''
        #pre-processing of the input paragraph
        new_para=''.join([lower(val) if val.isalnum() else ' ' for val in paragraph])
        para_lower=[i for i in new_para.split(' ') if len(i)<>0 ]
        for i in set(para_lower):
                if i not in banned:
                    collector[i]=para_lower.count(i)
        #return max(collector.keys(),key=lambda x: collector[x])
        return max(collector.keys(),key=collector.get)
            

        