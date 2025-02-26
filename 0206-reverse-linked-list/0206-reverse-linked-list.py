# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        while head:
            if (not head.next) or (not head):
                return head
            else:
                new_head=self.reverseList(head.next)
                head.next.next=head
                head.next=None
                return new_head
        
            
        