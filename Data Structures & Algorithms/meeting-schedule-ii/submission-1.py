"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        n = len(intervals)
        if n == 1:
            return 1

        times = set()
        for i in intervals:
            if i.start not in times:
                times.add(i.start)

            if i.end not in times:
                times.add(i.end)

        times = list(times)
        times.sort()
        times = [[t, 0] for t in times]

        for i in intervals:
            for t in times:
                if i.start <= t[0] and i.end > t[0]:
                    t[1] += 1

        max_rooms = 0
        for t in times:
            if t[1] > max_rooms:
                max_rooms = t[1]

        return max_rooms

