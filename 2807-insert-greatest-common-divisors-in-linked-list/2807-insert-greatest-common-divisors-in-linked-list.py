class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        current = head
        while current and current.next:
            gcd_value = math.gcd(current.val, current.next.val)
            gcd_node = ListNode(val=gcd_value)
            gcd_node.next = current.next
            current.next = gcd_node
            current = gcd_node.next
        
        return head