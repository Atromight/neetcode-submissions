class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while True:
            if n in nums:
                return False

            nums.add(n)

            s = str(n)
            n = sum([int(num) ** 2 for num in s])

            if n == 1:
                return True
