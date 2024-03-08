# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = collections.defaultdict(int)
        while head:
            freq[head.val] += 1
            head = head.next
        dummy = ListNode(0)
        cur = dummy
        for v in freq.values():
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

