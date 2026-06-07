class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        if not intervals:
            return [[start, end]]

        n = len(intervals)
        if start > intervals[n-1][1]:
            intervals.append([start, end])
            return intervals

        i = 0
        insert_idx = None
        while True:
            if not intervals:
                return [[start, end]]

            n = len(intervals)
            print(f"i: {i}, n: {n}, intervals: {intervals}, [start, end]: {[start, end]}")
            if i >= n:
                break

            cur_start, cur_end = intervals[i]
            if end < cur_start:
                insert_idx = i
                break

            else: # end >= cur_start:
                if start > cur_end:
                    i += 1
                    continue

                else: # start <= cur_end:
                    # The 2 intervals will have to be merged
                    start = min(cur_start, start)
                    end = max(cur_end, end)
                    intervals.pop(i)

        if insert_idx is not None:
            intervals.insert(insert_idx, [start, end])

        return intervals

