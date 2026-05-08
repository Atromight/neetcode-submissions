class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [target - num for num in nums]
        for i in range(0, len(nums)):
            if nums[i] in new_nums:
                # print("i: ", i)
                # print("nums[i]: ", nums[i])
                # print("nums[i]: ", nums[i])
                if new_nums.index(nums[i]) != i:
                    if i > new_nums.index(nums[i]):
                        return [new_nums.index(nums[i]), i]
                    else:
                        return [i, new_nums.index(nums[i])]

        