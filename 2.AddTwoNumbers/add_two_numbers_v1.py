from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = Solution.listNodeToNumber(l1)
        n2 = Solution.listNodeToNumber(l2)
        sum = n1+n2
        return Solution.numberToListNode(sum)

    @staticmethod
    def listNodeToNumber(lt: Optional[ListNode]) -> int:
        number = 0
        if lt is None:
            return number
        else:
            digits = ""
            while lt is not None:
                digits += str(lt.val)
                lt = lt.next
            number = int(''.join(reversed(digits)))
            return number

    @staticmethod
    def numberToListNode(number: int) -> ListNode:
        digits = str(number)
        head = ListNode(int(digits[-1]))
        current = head
        for digit in reversed(digits[:-1]):
            digitNode = ListNode(int(digit))
            current.next = digitNode
            current = digitNode
        return head

    @staticmethod
    def printListNode(lt: Optional[ListNode]):
        digits = ""
        while lt is not None:
            digits+=str(lt.val)
            lt = lt.next
        print(''.join(reversed(digits)))

if __name__ == "__main__":
    lt = ListNode(1, ListNode(2, ListNode(3)))
    number = Solution.listNodeToNumber(lt)
    print(number)
    Solution.printListNode(lt)