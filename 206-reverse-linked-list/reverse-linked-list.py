# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=None

        while head:
            '''None <- 1 <- 2 <- 3    4 -> 5 -> None
                                 ^    ^
                                prev curr
            '''
            #delete the link between head and heat.next
            temp=head.next
            head.next=node
            #update the value +1 step ahead and repeat the process till head is None
            node=head
            head=temp
        return node