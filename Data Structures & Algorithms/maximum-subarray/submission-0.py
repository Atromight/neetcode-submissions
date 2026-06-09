class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        any_positives = False
        for num in nums:
            if num > 0:
                any_positives = True
        
        if not any_positives:
            return max(nums)

        cur_sum = nums[0]
        max_sum = nums[0]
        # i = 0
        n = len(nums)
        # j = 0

        for i in range(1, n):
        # while i < n and j <= i:
            num = nums[i]
            # print(f"num: {num}, cur_sum: {cur_sum}, max_sum: {max_sum}")
            if num < 0:
                if cur_sum >= 0:
                    max_sum = max(cur_sum, max_sum)
                    if cur_sum - abs(num) >= 0:
                        cur_sum -= abs(num)

                    else: # cur_sum - abs(num) < 0
                        cur_sum = num

                else: # cur_sum < 0
                    if cur_sum < num:
                        cur_sum = num
                        max_sum = max(cur_sum, max_sum)

                    else: # cur_sum > num
                        max_sum = max(cur_sum, max_sum)
                        cur_sum = num

            else: # num >= 0
                if cur_sum < 0:
                    cur_sum = num
                    max_sum = max(cur_sum, max_sum)

                else: # cur_sum >= 0
                    cur_sum += num
                    max_sum = max(cur_sum, max_sum)

        return max_sum
        