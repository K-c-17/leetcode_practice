# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        while head and head.val==val:
            head=head.next
        
        current=head
        prev_node=None

        while current:
            if current.val==val:
                prev_node.next=current.next
            else:
                prev_node=current
            current=current.next
        
        return head

        