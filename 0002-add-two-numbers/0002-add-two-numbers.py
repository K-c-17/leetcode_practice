# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        index,curr1,curr2,sentinel,carry=0,l1,l2,ListNode(),0

        start=sentinel

        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            pair_sum=val1 + val2 + carry
            start.next=ListNode(pair_sum % 10)
            carry=pair_sum // 10

            curr1=curr1.next if curr1 else None
            curr2=curr2.next if curr2 else None
            start=start.next
        
        # if carry>0:
        #     start.next=ListNode(carry)
        
        return sentinel.next


        

        