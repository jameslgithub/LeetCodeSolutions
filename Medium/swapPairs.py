# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        prev = dummy
        temp = head

        while temp != None and temp.next != None:
            prev.next = temp.next
            temp.next = prev.next.next
            prev.next.next = temp

            prev = temp
            temp = temp.next
        return dummy.next
        
