class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while True:
            i = (l + r) // 2
            if target > nums[i]:
                l = i
            elif target < nums[i]:
                r = i
            else: # target == nums[i]
                return i
            
            if r == l:
                if nums[l] == target:
                    return l
                else:
                    return -1

            elif r - l == 1:
                if nums[r] == target:
                    return r
                elif nums[l] == target:
                    return l
                else:
                    return -1


        