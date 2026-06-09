class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        n = len(nums)

        for i in range(1, n):
            num = nums[i]
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
