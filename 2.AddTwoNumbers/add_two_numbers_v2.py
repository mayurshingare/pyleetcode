from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 800.1
# 9.
# 0
#

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carry = 0
        while l1 is not None or l2 is not None or carry!=0:
            l1.val += carry
            if l2 is not None:
                l1.val += l2.val
                l2 = l2.next

            carry, l1.val = divmod(l1.val, 10)

            if l1.next is None and (carry!=0 or l2 is not None):
                l1.next = ListNode(carry)
                carry = 0
            l1 = l1.next
        return head

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carry = 0
        while l1 is not None or l2 is not None or carry!=0:
            l1.val += carry

            if l2 is not None:
                l1.val += l2.val
                l2 = l2.next

            carry, l1.val = divmod(l1.val, 10)

            if l1.next is None and (carry!=0 or l2 is not None):
                l1.next = ListNode(carry)
                carry = 0
            l1 = l1.next
        return head