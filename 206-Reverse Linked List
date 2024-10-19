class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev
        
