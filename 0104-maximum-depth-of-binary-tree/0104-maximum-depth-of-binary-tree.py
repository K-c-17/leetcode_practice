# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue=collections.deque()
        queue.append((root,1))

        while queue:
            current,level=queue.popleft()
            if current.left:
                queue.append((current.left,level+1))
            if current.right:
                queue.append((current.right,level+1))
        print("level",level)
        return level
            

        

        
        