# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        queue=collections.deque()
        queue.append(root)
        output=[]

        while queue:
            max_val=float("-inf")
            for _ in range(len(queue)):
                current=queue.popleft()
                if current.val>max_val:
                    max_val=current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            output.append(max_val)
        return output





















        '''
        if not root:
            return []
        queue=collections.deque()
        queue.append(root)
        result=[]

        while queue:
            var=float("-inf")
            for i in range(len(queue)):
                current=queue.popleft()
                if current.val>var:
                    var=current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(var)
        return result
        '''