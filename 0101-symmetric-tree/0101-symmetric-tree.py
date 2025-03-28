# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        #Iterative Implementation
        if not root:
            return True
        
        queue=collections.deque()
        queue.append(root)

        while queue:
            temp=[]
            for i in range(len(queue)):
                curr=queue.popleft()
                if curr:
                    temp.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    temp.append(None)
            
            #print(temp)
            if temp!=temp[::-1]:
                return False
        
        return True


        
        
        
        
        
        
        
        
        
        #Recursive Implementation
        '''
        def is_mirror(node1,node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            
            return (node1.val==node2.val and 
            is_mirror(node1.left,node2.right) and
            is_mirror(node1.right,node2.left))

        return is_mirror(root,root)
        '''

        
        
        