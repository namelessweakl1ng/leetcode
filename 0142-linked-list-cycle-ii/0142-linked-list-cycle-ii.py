# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        curr = head
        lookup = set()
        
        while curr:
            if curr in lookup:
                return curr
            lookup.add(curr)
            curr = curr.next
        return None