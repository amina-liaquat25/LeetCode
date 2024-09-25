class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
            if s==f:
                return True
            
        return False  
