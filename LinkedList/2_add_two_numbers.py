class Solution:
    def addTwoNumbers(self, l1, l2):
        res = []
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l1.val if l2 else 0

            total = l1_val + l2_val + carry
            carry = total //10
            new_node = total % 10
            curr.next = new_node
            curr = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


