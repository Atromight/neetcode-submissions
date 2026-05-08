class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return 1

        i = 0
        j = 1
        longest_max = 0
        seen = {s[0]: 0}
        while i <= j and j < n:
            if s[j] in seen and seen[s[j]] >= i:
                if j == n - 1 and j - i > longest_max:
                    longest_max = j - i

                elif j - i > longest_max:
                    longest_max = j - i

                i = seen.pop(s[j]) + 1

            elif j == n - 1:
                if j - i + 1 > longest_max:
                    longest_max = j - i + 1

            seen[s[j]] = j
            j += 1

        return longest_max
