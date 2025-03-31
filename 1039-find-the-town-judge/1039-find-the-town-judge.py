class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        if n==1:
            return 1 if not trust else -1
            
        dependent=set()
        nums_of_depend=defaultdict(int)

        for i in trust:
            nums_of_depend[i[1]]+=1
            dependent.add(i[0])
        
        # print(nums_of_depend)
        # print(dependent)

        for j in nums_of_depend:
            if j not in dependent and nums_of_depend[j]==n-1:
                return j
        
        return -1

        