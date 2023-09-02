# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
# self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        tail = temp
        summer = 0

        while l1 is not None or l2 is not None or summer != 0:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0
            tot = num1 + num2 + summer
            digit = tot % 10
            summer = tot // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = temp.next
        temp.next = None
        return result
