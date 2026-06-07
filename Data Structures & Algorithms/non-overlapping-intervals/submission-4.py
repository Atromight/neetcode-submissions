class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        interval = intervals.pop()
        start = interval[0]
        n = len(intervals)
        res = 0
        for i in range(n-1, -1, -1):
            end = intervals[i][1]
            if start < end:
                res += 1

            else: # start >= end
                start = intervals[i][0]

        return res
