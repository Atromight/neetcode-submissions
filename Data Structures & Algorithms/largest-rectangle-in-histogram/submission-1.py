class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []
        for i in range(0, n):
            if stack:
                if heights[i] > stack[-1][0]:
                    stack.append([heights[i], i])

                elif heights[i] < stack[-1][0]:
                    while stack and heights[i] < stack[-1][0]:
                        # If the next height is less than the previous one in the stack,
                        # we need to remove the one in the stack and calculate the max area
                        # for that height (it's as good as it gets for that height in that pos)
                        height, pos = stack.pop()
                        area = height * (i - pos)
                        if max_area < area:
                            max_area = area

                    # We want the current height to take the earliest possible pos
                    # (This is the pos of the earliest height that curr height eliminated)
                    stack.append([heights[i], pos])

            else:
                stack.append([heights[i], i])

        while stack:
            height, pos = stack.pop()
            area = height * (n - pos)
            if max_area < area:
                max_area = area

        return max_area
        