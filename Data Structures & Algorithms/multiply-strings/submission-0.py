class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)
        digit_map = {
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
        }
        num1_int = 0
        mult = 1
        for i in range(m):
            digit = digit_map[num1[m-1-i]]
            num1_int += (digit * mult)
            mult *= 10
        
        num2_int = 0
        mult = 1
        for i in range(n):
            digit = digit_map[num2[n-1-i]]
            num2_int += (digit * mult)
            mult *= 10
        
        return str(num1_int * num2_int)


        