class ListNode:


class Solution:
    def merge(self, list1, list2):
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1.val
                list1, cur = list1.next, list1
            else:
                cur.next = list2.val
                list2, cur = list2.next, list2
        if list1 or list2:
            cur.next = list1 if list1 else list2
        return dummy.next
