# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head.next
        ret = header = ListNode()
        while cur is not None:
            total = 0
            while cur.val != 0:
                total += cur.val
                cur = cur.next
            header.next= ListNode(total)
            header = header.next

            cur = cur.next
        return ret.next 

        
