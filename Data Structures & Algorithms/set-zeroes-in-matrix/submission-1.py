class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        row_zeroes = set()
        col_zeroes = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zeroes.add(i)
                    col_zeroes.add(j)

        for x in row_zeroes:
            for j in range(n):
                matrix[x][j] = 0

        for y in col_zeroes:
            for i in range(m):
                matrix[i][y] = 0
