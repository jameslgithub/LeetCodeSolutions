# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)
                
        cur = head
        while cur is not None and cur.next is not None:
            gcd1 = gcd(cur.val, cur.next.val)
            cur.next = ListNode(gcd1, cur.next)
            cur = cur.next.next
        return head
