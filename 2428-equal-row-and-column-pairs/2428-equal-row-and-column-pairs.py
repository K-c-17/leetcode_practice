class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        collector=Counter([tuple(i) for i in grid])

        final=0

        for j in zip(*grid):
            final+=collector[tuple(j)]
        
        return final
        