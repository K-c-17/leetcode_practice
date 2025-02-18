# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_dia=[0]
        self.helper_func(root,max_dia)

        return max_dia[0]

    def helper_func(self,root,max_dia):
        if not root:
            return 0
        
        left_height=self.helper_func(root.left,max_dia)
        right_height=self.helper_func(root.right,max_dia)

        max_dia[0]=max(max_dia[0],left_height+right_height)

        return 1+ max(left_height,right_height)
        

        