class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # collector={}
        # for word in strs:
        #     collector[word]=sorted(list(word))
        # print(collector)
        # common={}
        # result=[]
        
        # for i in collector:
        #     if collector[i] not in common:
        #         common[collector[i]] = [i]
        #     else:
        #         common[collector[i]].append(i)
        # print(common)



        #     for j in common:
        #         if collector[i]==common[j]:
        #             result.append([i,j])
        #             del common[j]
        #         else:
        #             print(1)
        #             common[i]=collector[i]
        # return result

        sorted_list=[''.join(sorted(i)) for i in strs]

        collector={}
        # for i in range(len(sorted_list)):
        #     if sorted_list[i] not in collector:
        #         collector[sorted_list[i]]=[strs[i]]
        #     else:
        #         collector[sorted_list[i]].append(strs[i])
        
        #print(collector)

        #return [x for x in collector.values()]
        #    collector[sorted_list[i]]

        for val1,val2 in zip(sorted_list,strs):
            if val1 not in collector.keys():
                collector[val1]=[val2]
            else:
                collector[val1].append(val2)
        
        return collector.values()

            


        


        