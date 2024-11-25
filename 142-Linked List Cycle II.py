class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = s = head
        while f and f.next:
            s, f = s.next, f.next.next
            if f == s:
                # return True
                s = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
        return None
