# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue=collections.deque()
        queue.append((root,1))
        max_length=float("-inf")

        while queue:
            temp=[]
            for _ in range(len(queue)):
                current,alias=queue.popleft()
                temp.append(alias)
                if current.left:
                    queue.append((current.left,alias*2))
                if current.right:
                    queue.append((current.right,(alias*2)+1))
            
            length=temp[-1]-temp[0]+1
            
            if length>max_length:
                max_length=length

        
        return max_length


















        '''
        if not root:
            return 0
        queue = collections.deque()
        queue.append((root,1,0))
        max_width=float('-inf')

        while queue:
            for i in range(len(queue)):
                current,num,level=queue.popleft()
                if i==0:
                    start=num
                if current.left:
                    queue.append((current.left,num*2,level+1))
                if current.right:
                    queue.append((current.right,num*2+1,level+1))
            if (num-start)+1>max_width:
                max_width=(num-start)+1
        
        return max_width
        '''
            
            



        