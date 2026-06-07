class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        while intervals:
            cur_start, cur_end = intervals.pop()
            i = 0
            n = len(res)
            merged = False
            while i < n:
                start, end = res[i]
                if start <= cur_end and end >= cur_start:
                    start = min(cur_start, start)
                    end = max(cur_end, end)
                    res[i] = [start, end]
                    merged = True

                i += 1

            if not merged:
                res.append([cur_start, cur_end])

        duplicates = set()
        uniques = []
        for start, end in res:
            if (start, end) in duplicates:
                continue

            duplicates.add((start, end))
            uniques.append([start, end])

        return uniques
