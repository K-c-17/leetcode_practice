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
        curr_node=head
        prev_node=None
        while curr_node is not None:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node
        return prev_node
            
        