# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=collections.deque()
        queue.append((root,0))
        col_map={}
        while queue:
            current,col=queue.popleft()
            if col not in col_map.keys():
                col_map[col]=[current.val]
            else:
                col_map[col].append(current.val)
            if current.left:
                queue.append((current.left,col-1))
            if current.right:
                queue.append((current.right,col+1))

        sor_list=sorted([x for x in col_map.keys()])
        final=[]
        for i in sor_list:
            final.append(col_map[i])
        
        return final

        