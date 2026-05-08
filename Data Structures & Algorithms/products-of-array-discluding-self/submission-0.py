class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        response = [1] * len(nums)
        prod = 1
        zero_pos = []
        for i, num in enumerate(nums):
            if num == 0:
                zero_pos.append(i)
            else:
                prod *= num

        if len(zero_pos) > 1:
            response = [0] * len(nums)
        elif len(zero_pos) == 1:
            response = [0] * len(nums)
            i = zero_pos[0]
            response[i] = prod
        # no zeroes in nums
        else:
            for i, num in enumerate(nums):
                response[i] = int(prod/nums[i])

        return response
        
        

        