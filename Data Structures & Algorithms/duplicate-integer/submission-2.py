class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        if len(unique) == len(nums):
            return False
        else:
            return True
        