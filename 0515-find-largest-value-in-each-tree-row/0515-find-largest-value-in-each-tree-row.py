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
        final=[]
        while queue:
            temp=[]
            for _ in range(len(queue)):
                current=queue.popleft()
                temp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            final.append(max(temp))
        return  final

















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