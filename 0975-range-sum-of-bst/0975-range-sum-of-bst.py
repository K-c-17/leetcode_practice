# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        self.total=0
        self.dfs_helper(root,low,high)
        return self.total
        #####BFS
        # queue=collections.deque()
        # queue.append(root)
        # total=0
        # while queue:
        #     curr=queue.popleft()
        #     if curr.val >= low and curr.val <= high:
        #         total+=curr.val
        #     if curr.left:
        #         queue.append(curr.left)
        #     if curr.right:
        #         queue.append(curr.right)
        
        # return total
    #####DFS
    # def dfs_helper(self,root,low,high):
    #     if not root:
    #         return
    #     if root.val>=low and root.val<=high:
    #         self.total+=root.val
    #     self.dfs_helper(root.left,low,high)
    #     self.dfs_helper(root.right,low,high)

    #DFS on BST
    def dfs_helper(self,root,low,high):
        if not root:
            #print("Hit the leaf")
            return
        if root.val<low:
            self.dfs_helper(root.right,low,high)
            return
        elif root.val>high:
            self.dfs_helper(root.left,low,high)
            return
        else:
            #print("Pre-add total:",self.total)
            #print("Value added",root.val)
            self.total+=root.val
            #print("Post-add total:",self.total)
            self.dfs_helper(root.left,low,high)
            self.dfs_helper(root.right,low,high)