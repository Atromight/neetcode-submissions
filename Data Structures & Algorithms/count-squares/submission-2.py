class CountSquares:
    def __init__(self):
        # Count keeps track of extra appearances of points
        self.cnt = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point in self.cnt:
            self.cnt[point] += 1
        else:
            self.cnt[point] = 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for i, j in self.cnt:
            if (
                (i < x and j < y) or
                (i > x and j > y) or
                (i < x and j > y) or
                (i > x and j < y)
            ):
                if (
                    abs(x-i) == abs(y-j) and
                    (i, y) in self.cnt and (x, j) in self.cnt
                ):
                    res += (self.cnt[(i, j)] * self.cnt[(i, y)] * self.cnt[(x, j)])

        return res
