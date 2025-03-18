# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # output=[]
        # self.inorder_helper(root,output)
        # return output

    # def inorder_helper(self,root,output):
    #     if root:
    #         self.inorder_helper(root.left,output)
    #         output.append(root.val)
    #         self.inorder_helper(root.right,output)
        stack,current=[],root
        output=[]

        while stack or current:
            while current:
                stack.append(current)
                current=current.left
            current=stack.pop()
            output.append(current.val)
            current=current.right
        
        return output




















    '''
        output=[]
        stack=[]
        current=root

        while current or stack:
            while current:
                stack.append(current)
                current=current.left
            current=stack.pop()
            output.append(current.val)
            current=current.right
        
        return output
    '''

        