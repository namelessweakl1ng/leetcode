# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow = fast = head
        # go fast and slow to find the middle in the slow
        while fast and fast.next: # loop till the fast is at the last node or the null
            slow = slow.next
            fast = fast.next.next
        # rotate the 2nd half of the list
        prev = None
        while slow: # till the slow becomes null
            temp = slow.next
            slow.next= prev
            prev= slow
            slow = temp
        # after rotating compare it and return
        left,right = head, prev # prev will be at the end and the slow will be null
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right  = right.next
        return True