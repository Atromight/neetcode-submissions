class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        n = len(intervals)
        m = len(queries)
        total_start = intervals[0][0]
        total_end = intervals[0][1]
        for i in intervals:
            if i[0] < total_start:
                total_start = i[0]

            if i[1] > total_end:
                total_end = i[1]

        res = [10001] * m
        # print(f"intervals: {intervals}")
        # print(f"queries: {queries}")
        for j in range(m):
            q = queries[j]
            if q >= total_start and q <= total_end:
                for i in range(n):
                    if q >= intervals[i][0] and q <= intervals[i][1]:
                        length = intervals[i][1] - intervals[i][0] + 1
                        if length < res[j]:
                            res[j] = length

            if res[j] == 10001:
                res[j] = -1

        return res

