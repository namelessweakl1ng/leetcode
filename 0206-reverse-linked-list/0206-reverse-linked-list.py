# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None
        while curr: # for example [1,2]
            tmp = curr.next # tmp = 2
            curr.next = prev # 1->null
            prev = curr # prev = 1 
            curr = tmp # move the curr to next that is 2 and repeat till the curr is goes to null
        return prev
