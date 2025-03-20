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

        while curr1 and curr2:
            pair_sum=curr1.val + curr2.val + carry
            start.next=ListNode(pair_sum % 10)
            carry=pair_sum // 10

            curr1=curr1.next
            curr2=curr2.next
            start=start.next
        
        while curr1:
            pair_sum=curr1.val+carry
            start.next=ListNode(pair_sum % 10)
            carry=pair_sum // 10

            curr1=curr1.next
            start=start.next
        
        while curr2:
            pair_sum=curr2.val+carry
            start.next=ListNode(pair_sum % 10)
            carry=pair_sum // 10

            curr2=curr2.next
            start=start.next
        
        if carry>0:
            start.next=ListNode(carry)
        
        return sentinel.next


        

        