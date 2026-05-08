class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            i = (l + r) // 2
            if l == r:
                return nums[l]

            if nums[l] > nums[r]:
                if r - l == 1:
                    l = r
                else:
                    if nums[i] > nums[r]:
                        l = i
                    elif nums[i] < nums[r]:
                        r = i

            elif nums[l] < nums[r]:
                r = i
