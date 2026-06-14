class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        grid = [[0] * n for _ in range(m)]

        i = 0
        j = 0
        while i < m and j < n:
            if i == 0 or j == 0:
                grid[i][j] = max(grid[i][j], 0)

            else:
                grid[i][j] = max(grid[i-1][j-1], grid[i][j])

            if text1[i] == text2[j]:
                if i == 0 or j == 0:
                    grid[i][j] = 1

                else:
                    grid[i][j] = grid[i-1][j-1] + 1

                for x in range(i+1, m):
                    if grid[i][j] >= grid[x][j]:
                        grid[x][j] = grid[i][j]

                    else: # grid[i][j] < grid[x][j]
                        break

                for y in range(j+1, n):
                    if grid[i][j] >= grid[i][y]:
                        grid[i][y] = grid[i][j]

                    else: # grid[i][j] < grid[x][j]
                        break

            j += 1
            if j == n:
                j = 0
                i += 1

        return grid[m-1][n-1]
