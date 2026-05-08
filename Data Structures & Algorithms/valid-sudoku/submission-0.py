class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check all rows valid
        for i in range(0, 9):
            nums = [str(x) for x in range(1, 10)]
            for j in range(0, 9):
                num = board[i][j]
                if num != ".":
                    if num not in nums:
                        return False

                    else:
                        nums.remove(num)

        # Check all columns valid
        for i in range(0, 9):
            nums = [str(x) for x in range(1, 10)]
            for j in range(0, 9):
                num = board[j][i]
                if num != ".":
                    if num not in nums:
                        return False

                    else:
                        nums.remove(num)

        # Check all squares valid
        for pos_x, pos_y in [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6),
        ]:
            nums = [str(x) for x in range(1, 10)]
            for i in range(pos_x, pos_x + 3):
                for j in range(pos_y, pos_y + 3):
                    num = board[i][j]
                    if num != ".":
                        if num not in nums:
                            return False

                        else:
                            nums.remove(num)

        return True

        



                
        