# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        first = second = head
        
        #Find halfway
        while first and first.next:
            first = first.next.next
            second = second.next
                
        #Reverse second half
        temp = second 
        second = second.next
        temp.next = prev = None
        
        while second:
            temp = second.next 
            second.next = prev
            prev = second 
            second = temp
        
        second = prev    
        first = head    
        #Merge lists to reorder
        while second:
            temp = second.next
            second.next = first.next
            first.next = second
            first = first.next.next
            second = temp
        
        
             
            