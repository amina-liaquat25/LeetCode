# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0) 

        curr=dummy

        c=0 

        #run while loop till the length of list 1 or list 2 or till no carry
        while(l1 or l2 or c):

            if(l1):
                c+=l1.val
                l1=l1.next

            if(l2):
                c+=l2.val
                l2=l2.next

            #it is storing the value of sum
            curr.next=ListNode(c%10) #creating a new node here

            #curr is pointing to an Node at head
            curr=curr.next

            #it is storing carry
            c=c//10

        return dummy.next
