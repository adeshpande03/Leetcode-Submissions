#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        il = [head]
        c = 1
        while head.next:
            head = head.next
            il.append(head)
        return (il[len(il)//2])
        