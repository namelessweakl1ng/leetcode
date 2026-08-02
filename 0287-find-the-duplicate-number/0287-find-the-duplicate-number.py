class Solution(object):
    def findDuplicate(self, nums):
        # using floyd's algorithm we use slow and fast to find the start for the loop and return the value
        slow = fast =0

        while True: #cuz we know that its garunteed that there will be a loop
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        # after we get the P and the X in the linked list based on the algorithm 
        # we move both the slow and the index from the 0 they will meet at the beggening
        slow2 = 0
        while slow!=slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow