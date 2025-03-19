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
        collector=[]
        current=head
        prev_node=None

        while current:
            temp=current.next
            if current.val not in collector:
                collector.append(current.val)
                prev_node=current
            else:
                prev_node.next=current.next
                current.next=None
            current=temp
        
        return head


        