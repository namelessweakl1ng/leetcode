class MyCalendarTwo(object):

    def __init__(self):
        self.overlapping = []
        self.non_overlapping = []

    def book(self, startTime, endTime):
        for s,e in self.overlapping: 
            if max(s,startTime) < min(e, endTime): # check weather it overlaps if yes then you will return false
                return False
        
        for s,e in self.non_overlapping:
            if max(s,startTime) < min(e, endTime):
                self.overlapping.append(
                    (max(s,startTime),min(e, endTime)) # converting into a tuple before appending
                )
        self.non_overlapping.append((startTime,endTime)) # if none of the loops execute then the start and end time will be appended
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)