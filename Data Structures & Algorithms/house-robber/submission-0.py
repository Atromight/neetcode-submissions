class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * (n + 1)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]
        curr_max = max(dp[2], dp[1])
        if n == 3:
            return curr_max

        for i in range(3, n):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
            if dp[i] > curr_max:
                curr_max = dp[i]

        return curr_max
