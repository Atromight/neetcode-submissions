class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            i = (l + r) // 2
            if target == nums[i]:
                return i
            elif target == nums[l]:
                return l
            elif target == nums[r]:
                return r

            if l == r:
                if target == nums[l]:
                    return l
                else:
                    return -1
            
            if r - l == 1:
                if target == nums[l]:
                    return l
                elif target == nums[r]:
                    return r
                else:
                    return -1
                

            if nums[l] > nums[r]:
                if target < nums[l] and target > nums[r]:
                    return -1

                if nums[i] > nums[r]:
                    if target < nums[l] or target > nums[i]:
                        l = i
                    elif target > nums[l] and target < nums[i]:
                        r = i
                    elif target > nums[l] and target > nums[i]:
                        l = i

                elif nums[i] < nums[r]:
                    if target > nums[i] and target < nums[r]:
                        l = i
                    elif target < nums[i] or target > nums[r]:
                        r = i

            elif nums[l] < nums[r]:
                if target < nums[l] or target > nums[r]:
                    return -1

                else: # target > nums[l] and target < nums[r]
                    if target < nums[i]:
                        r = i
                    elif target > nums[i]:
                        if r - l == 1:
                            l = r
                        else:
                            l = i
                    else: # target == nums[i]
                        return i
