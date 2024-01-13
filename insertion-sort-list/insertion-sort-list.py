class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = head

        while current and current.next:
            if current.val > current.next.val:
                prev = dummy
                while prev.next.val < current.next.val:
                    prev = prev.next

                temp = current.next
                current.next = temp.next
                temp.next = prev.next
                prev.next = temp
            else:
                current = current.next

        return dummy.next