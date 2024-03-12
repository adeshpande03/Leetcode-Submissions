class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0, head)
        current = dummy
        prefix_sum = 0
        prefix_to_node = {}

        # Compute prefix sums and store the nodes in a dictionary
        while current:
            prefix_sum += current.val
            prefix_to_node[prefix_sum] = current
            current = current.next

        # Reset prefix sum and pointer to dummy node
        prefix_sum = 0
        current = dummy

        # Adjust pointers based on prefix sums
        while current:
            prefix_sum += current.val
            current.next = prefix_to_node[prefix_sum].next
            current = current.next

        return dummy.next
