class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr: str, n: int, k: int) -> None:
            if n == 0 and k == 0:
                res.append(curr)

            elif n == 0: # k != 0
                backtrack(curr + ")", n, k-1)

            elif k == 0: # n != 0
                backtrack(curr + "(", n-1, k+1)

            else: # n != 0 and k != 0
                backtrack(curr + "(", n-1, k+1)

                backtrack(curr + ")", n, k-1)

            return


        backtrack("", n, 0)

        return res
