# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        #dummy=ListNode()
        #tail=dummy
        output=[]

        while head:
            output.append(head.val)
            head=head.next
        start=0
        end=len(output)-1
        while end>=start:
            if output[start]!=output[end]:
                return False
            start+=1
            end-=1
        return True
        
        