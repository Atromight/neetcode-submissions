class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        PHONE_MAP = {
            "2": set(["a", "b", "c"]),
            "3": set(["d", "e", "f"]),
            "4": set(["g", "h", "i"]),
            "5": set(["j", "k", "l"]),
            "6": set(["m", "n", "o"]),
            "7": set(["p", "q", "r", "s"]),
            "8": set(["t", "u", "v"]),
            "9": set(["w", "x", "y", "z"]),
        }
        if digits == "":
            return []

        def backtrack(i: int, curr: str):
            if i == n:
                res.append(curr)
                return

            digit = digits[i]
            letters = PHONE_MAP[digit]
            for letter in letters:
                backtrack(i+1, curr + letter)

            return


        backtrack(0, "")

        return res














