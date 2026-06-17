class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        limit = n
        for i in range(n // 2):
            limit -= 1
            for j in range(i, limit):
                print((i,j))
                matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i],     matrix[i][j] =\
                matrix[i][j],     matrix[j][n-1-i],     matrix[n-1-i][n-1-j], matrix[n-1-j][i]
