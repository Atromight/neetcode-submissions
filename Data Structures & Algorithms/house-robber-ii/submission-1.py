class Solution:
    def rob(self, nums: List[int]) -> int:
        def find_max(dp1: list, dp2: list) -> list:
            if dp1[0] > dp2[0]:
                return dp1
            elif dp2[0] > dp1[0]:
                return dp2
            else: # dp1[0] == dp2[0]
                if not dp1[1] or not dp2[1]:
                    return [dp1[0], False]
                else:
                    return [dp1[0], True]

        n = len(nums)
        if n <= 3:
            return max(nums)

        if n == 4:
            return max(nums[0] + nums[2], nums[1] + nums[3])

        # n >= 5
        dp = [[0, False]] * (n + 1) # dp = [max_val, contains_0]
        dp[0] = [nums[0], True]
        dp[1] = [nums[1], False]
        dp[2] = [nums[2] + nums[0], True]
        # is_zero tracks whether the current sp sum has taken included the first house
        # (i.e. house with index zero is in sum)
        total_max, is_zero = find_max(dp[1], dp[2])
        for i in range(3, n):
            if i == n-1:
                # I want to potentially remove house 0's loot from the sums before deciding maximum
                if dp[i-2][1]:
                    dp[i-2][0] = dp[i-2][0] - nums[0]

                if dp[i-3][1]:
                    dp[i-3][0] = dp[i-3][0] - nums[0]

                curr_max, is_zero = find_max(dp[i-2], dp[i-3])

            else:
                curr_max, is_zero = find_max(dp[i-2], dp[i-3])

            dp[i] = [nums[i] + curr_max, is_zero]

            if dp[i][0] > total_max:
                total_max = dp[i][0]

        return total_max
