# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0,head)
        left = dummy
        right = head

        # move the right to the n point from the head
        while n > 0 and right:
            right = right.next
            n -=1
        # now according to the 2 pointers algorithm what you do is move both till the right hits null
        while right:
            left= left.next
            right = right.next
        # to delete the n item we simply update the list
        left.next= left.next.next
        # while returning exclude the dummy we added at the beggening
        return dummy.next