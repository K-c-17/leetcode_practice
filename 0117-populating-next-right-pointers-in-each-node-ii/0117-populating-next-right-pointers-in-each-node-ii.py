"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            prev_node=None
            for _ in range(len(queue)):
                current=queue.popleft()
                if prev_node:
                    prev_node.next=current
                prev_node=current
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return root
