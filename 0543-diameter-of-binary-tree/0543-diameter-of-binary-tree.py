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
        longest_path=[[]]
        self.helper_func(root,max_dia,longest_path)
        print(longest_path)
        return max_dia[0]

    def helper_func(self,root,max_dia,longest_path):
        if not root:
            return 0,[]
        
        left_height,left_path=self.helper_func(root.left,max_dia,longest_path)
        right_height,right_path=self.helper_func(root.right,max_dia,longest_path)

        if left_height+right_height>max_dia[0]:
            max_dia[0]=left_height+right_height
            longest_path[0]=left_path+[root.val]+right_path  
        
        if left_height>right_height:
            left_height+=1
            return left_height,left_path+[root.val]
        else:
            right_height+=1
            return right_height,right_path+[root.val]