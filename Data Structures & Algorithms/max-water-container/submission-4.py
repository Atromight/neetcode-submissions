class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        l = 0
        r = n-1
        while l < r:
            area = (r-l) * min([heights[r], heights[l]])
            if area > max_area:
                max_area = area
            
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                if heights[l+1] > heights[l]:
                    l += 1
                elif heights[r-1] > heights[r]:
                    r -= 1
                else:
                    l += 1
                    r -= 1
        
        return max_area

            
        