# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: float
        :rtype: int
        """
        queue=collections.deque()
        queue.append(root)
        
        self.closest=root.val
        self.distance=abs(target-root.val)
        
        while queue:
            curr=queue.popleft()
            if abs(target-curr.val) == self.distance:
                self.closest=min(self.closest,curr.val)
            elif abs(target-curr.val) < self.distance:
                self.closest=curr.val
                self.distance=abs(target-curr.val)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)        
        
        return self.closest
        
        