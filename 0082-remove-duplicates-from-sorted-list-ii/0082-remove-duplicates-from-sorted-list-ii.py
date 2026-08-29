class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        while current and current.next:
            if current.val == current.next.val:
                duplicate = current.val
                while current and current.val == duplicate:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next

        return dummy.next