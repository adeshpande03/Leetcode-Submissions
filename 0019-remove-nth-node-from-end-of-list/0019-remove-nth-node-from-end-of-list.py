# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans=ListNode(0)
        ans.next=head
        first=ans
        second=ans
        for i in range(1,n+2):
            second=second.next
        while(second is not None):
            second=second.next
            first=first.next
        first.next=first.next.next
        return ans.next