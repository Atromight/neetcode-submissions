class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        res = set()
        res.add((n-1, 0))
        for i in range(1, n):
            cur = nums[n-i-1]
            if n-i-1 + cur >= n-1:
                res.add((n-i-1, 1))

            else: # n-i-1 + cur < n-1
                length = n-i-1 + cur
                cur_jumps = n
                for pos, jumps in res:
                    if pos <= length:
                        cur_jumps = min(cur_jumps, jumps)

                res.add((n-i-1, cur_jumps+1))

        for pos, jumps in res:
            if pos == 0:
                return jumps





        
