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
        def show(lst):
            output_str=""
            while lst:
                output_str+=str(lst.val)+"->"
                lst=lst.next
            print(output_str)
        
        def reverse(lst):
            current=lst
            prev_node=None

            while current:
                temp=current.next
                current.next=prev_node
                prev_node=current
                current=temp
            return prev_node
        
        #rev_l1=reverse(l1)
        #rev_l2=reverse(l2)

        #show(rev_l1)
        #show(rev_l2)
        show(l1)
        show(l2)

        #index,curr1,curr2,sentinel,carry=0,rev_l1,rev_l2,ListNode(),0
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


        

        