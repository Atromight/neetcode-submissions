class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr: List[int], nums: List[int]):
            n = len(nums)
            # print("")
            # print("Remaining nums: ", nums)
            # print("curr: ", curr)
            if n == 1:
                curr.append(nums.pop())
                res.append(curr.copy())
                curr.pop()
                return

            print("")
            print("GOING IN FOR LOOP")           
            for i in range(n):
                print("curr: ", curr)
                print("nums[i]: ", nums[i])
                curr.append(nums[i])
                remaining = nums[:i] + nums[i+1:]
                print("remaining: ", remaining)
                backtrack(curr, remaining)
                curr.pop()


        backtrack([], nums)

        return res
        