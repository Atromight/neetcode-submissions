class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        u = 0
        d = m-1
        while u <= d:
            l = 0
            r = n-1
            j = (d + u) // 2
            if target < matrix[j][0]:
                if u == d:
                    return False
                else:
                    d = j

            elif target == matrix[j][0]:
                return True

            elif target > matrix[j][0] and target < matrix[j][-1]:
                row = matrix[j]
                while l <= r:
                    i = (l + r) // 2
                    if target == row[i]:
                        return True

                    else:
                        if l == r:
                            return False

                        if target < row[i]:
                            r = i

                        else: # target > row[i]
                            if r - l == 1:
                                l = r
                            else:
                                l = i

            elif target == matrix[j][-1]:
                return True

            elif target > matrix[j][-1]:
                if u == d:
                    return False

                elif d - u == 1:
                    u = d

                else:
                    u = j
        