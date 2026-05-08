class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        max_area = 0
        l_height = height[0]
        r_height = height[n-1]
        while l < r:
            if height[l] > height[r]:
                if height[r-1] < r_height:
                    max_area += r_height - height[r-1]
                elif height[r-1] > r_height:
                    r_height = height[r-1]

                r -= 1

            elif height[l] <= height[r]:
                if height[l+1] < l_height:
                    max_area += l_height - height[l+1]
                elif height[l+1] > l_height:
                    l_height = height[l+1]

                l += 1

        return max_area



        