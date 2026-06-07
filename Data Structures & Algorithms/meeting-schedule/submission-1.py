"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        interval = intervals.pop()
        start = interval.start
        n = len(intervals)
        for i in range(n-1, -1, -1):
            end = intervals[i].end
            if start < end:
                return False

            else:
                start = intervals[i].start

        return True
