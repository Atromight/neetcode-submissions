class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.n = len(nums)
        self.res = 0
        self.target = target
        i = 0
        def dfs(i: int, total: int) -> None:
            if i == self.n:
                if total == target:
                    self.res += 1

                return

            dfs(i+1, total + nums[i])
            dfs(i+1, total - nums[i])


        dfs(0, 0)

        return self.res
