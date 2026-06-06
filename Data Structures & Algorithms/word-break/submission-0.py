class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for word in word_set:
                t = len(word)
                if t > n-i:
                    continue

                for j in range(t):
                    if s[i + j] != word[j]:
                        break

                    if (j == t-1) and (s[i + j] == word[j]) and dp[i + j + 1]:
                        dp[i] = True


        return dp[0]
