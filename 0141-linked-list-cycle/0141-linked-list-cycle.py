# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current=head
        collector=set()
        
        while current:
            if current in collector:
                return True
            collector.add(current)
            current=current.next
        return False

        