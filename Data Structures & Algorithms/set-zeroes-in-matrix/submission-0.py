class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zeroes = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes.add((i, j))

        for x, y in zeroes:
            for j in range(n):
                matrix[x][j] = 0

            for i in range(m):
                matrix[i][y] = 0
