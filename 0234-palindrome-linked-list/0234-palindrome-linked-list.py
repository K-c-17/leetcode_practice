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
        '''
        output=[]

        while head:
            output.append(head.val)
            head=head.next
        return output==output[::-1]
        '''
        fast=head
        slow=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        prev_node=None
        
        while slow:
            temp=slow.next
            slow.next=prev_node
            prev_node=slow
            slow=temp
        
        start=head
        end=prev_node
        
        #print("Start of the loop:", start.val)
        #print("End of the loop:", end.val)

        while end:
            #print("value of start:",start.val,start.next)
            #print("value of end:",end.val,end.next)
            if start.val!=end.val:
                return False
            start=start.next
            end=end.next
        
        return True


        
        