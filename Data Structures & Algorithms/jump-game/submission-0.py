class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        j = 1
        for i in range(n-2, -1, -1):
            if i == 0 and nums[i] >= j:
                return True

            if nums[i] >= j:
                j = 1
            else:
                j += 1

        return False
