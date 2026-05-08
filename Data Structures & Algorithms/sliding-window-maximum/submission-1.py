class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        window = []
        for i in range(0, k):
            window.append(nums[i])

        res = [max(window)]
        i = 0
        j = k
        while i <= j and j < n:
            window.pop(0)
            i += 1

            window.append(nums[j])

            if nums[j] >= res[-1]:
                res.append(nums[j])
            else:
                res.append(max(window))

            j += 1


        return res




