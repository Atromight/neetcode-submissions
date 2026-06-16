class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for num in digits:
            s += str(num)

        i = int(s) + 1
        s = str(i)
        res = []
        for num in s:
            res.append(int(num))

        return res
