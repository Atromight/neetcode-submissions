class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        self.max_len = 1
        self.max_sub = s[0]
        self.visited = set()
        self.dfs(s, 0, n-1)
        return self.max_sub


    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(0, n//2):
            if s[i] != s[n-i-1]:
                return False

        return True


    def dfs(self, s: str, i: int, j: int) -> None:
        n = len(s)
        if (i, j) in self.visited:
            return

        self.visited.add((i, j))
        if self.isPalindrome(s):
            if n > self.max_len:
                self.max_len = n
                self.max_sub = s
        
        if n > 1 and n > self.max_len:
            self.dfs(s[:-1], i, j-1)
            self.dfs(s[1:], i+1, j)
        else:
            return




