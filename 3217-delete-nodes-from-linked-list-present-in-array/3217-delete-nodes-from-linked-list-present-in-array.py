class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(next = head)
        set_nums = set(nums)
        while node.next:
            if node.next.val in set_nums:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next     