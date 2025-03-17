# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        queue = collections.deque()
        queue.append(root)
        sum_at_level,level=float('-inf'),0
        
        while queue:
            temp=0
            level+=1
            for _ in range(len(queue)):
                current = queue.popleft()
                temp+=current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            if temp>sum_at_level:
                sum_at_level,min_level=temp,level
       
        return min_level

                
                
        