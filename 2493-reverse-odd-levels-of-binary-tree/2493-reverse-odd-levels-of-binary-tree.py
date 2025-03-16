# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        
        queue=collections.deque()
        queue.append(root)
        level=0
        result=[]

        while queue:
            temp=[]
            for i in range(len(queue)):
                current=queue.popleft()
                temp.append(current)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
           
            if level%2!=0:
                left=0
                right=len(temp)-1
                while left<right:
                    temp[left].val,temp[right].val=temp[right].val,temp[left].val
                    left+=1
                    right-=1           
            level+=1
        return root