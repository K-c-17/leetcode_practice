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
        queue.append((root,1))
        final=defaultdict()
        
        while queue:
            temp=0
            for i in range(len(queue)):
                current,level = queue.popleft()
                temp+=current.val
                if current.left:
                    queue.append((current.left,level+1))
                if current.right:
                    queue.append((current.right,level+1))
            final[level]=temp
        
        return max(final,key=final.get)

                
                
        