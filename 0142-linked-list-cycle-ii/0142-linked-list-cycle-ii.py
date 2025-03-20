# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current=head
        seen=set()

        while current:
            if current in seen:
                return current
            else:
                seen.add(current)
            
            current=current.next
        
        return None
        
        
        
        
        
        
        
        
        
        
        '''
        current=head
        seen=[]
        index=0

        while current:
            for i in seen:
                if current==i[0]:
                    return i[1]
            seen.append((current,index))
            index+=1
            current=current.next
        
        return None
        '''


        