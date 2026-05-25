class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        letters = list(s)
        n = len(letters)

        def is_palindrome(word: str) -> bool:
            m = len(word)
            for i in range(0, m//2):
                if word[i] != word[m-i-1]:
                    return False

            return True


        def backtrack(i: int, curr: List[str]):
            prev = curr[-1]
            if i == n:
                if is_palindrome(prev):
                    res.append(curr)
                # res.append(curr.copy())
                return

            letter = letters[i]
            print("")
            print("letter: ", letter)
            print("prev: ", prev)
            if is_palindrome(prev):
                backtrack(i+1, curr + [letter])

            curr[-1] += letter            
            backtrack(i+1, curr)

            return


        backtrack(1, [letters[0]])

        return res
        