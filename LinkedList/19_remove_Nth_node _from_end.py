class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # count the length of linked list
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head # don't change the input easily, you can do copy
        while first is not None:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

    # the second way to fingure out this question is not using dummy
    def removeNthFromEnd2(self, head, n):
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        fast = fast.next.next
        return head


