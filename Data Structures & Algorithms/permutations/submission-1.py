class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr: List[int], nums: List[int]):
            n = len(nums)
            if n == 1:
                curr.append(nums.pop())
                res.append(curr.copy())
                curr.pop()
                return
         
            for i in range(n):
                curr.append(nums[i])
                remaining = nums[:i] + nums[i+1:]
                backtrack(curr, remaining)
                curr.pop()

        backtrack([], nums)

        return res
        