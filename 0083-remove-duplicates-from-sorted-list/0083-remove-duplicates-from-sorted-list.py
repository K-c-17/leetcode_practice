# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current=head
        prev_node=None

        while current:
            if not prev_node or current.val != prev_node.val:
                prev_node=current
            else:
                prev_node.next=current.next
            current=current.next
        
        return head


        