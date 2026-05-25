class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        def backtrack(i: int, placed: set[tuple[int, int]], blocked: set[tuple[int, int]]) -> None:
            if i == n:
                if len(placed) == n:
                    solutions.append(placed.copy())

                return

            for j in range(n):
                curr_blocked = set()
                if (i, j) not in blocked:
                    placed.add((i, j))
                    # Block horizontals
                    for row in range(n):
                        if row != i:
                            curr_blocked.add((row, j))


                    # Block verticals
                    for col in range(n):
                        if col != j:
                            curr_blocked.add((i, col))

                    # Block diagonals
                    # I only block diagonals downwards
                    # (Because I start from the top row and move downstairs)
                    row = i + 1
                    col = j
                    k = 1
                    while row < n:
                        if col - k >= 0:
                            curr_blocked.add((row, col-k))

                        if col + k < n:
                            curr_blocked.add((row, col+k))

                        row += 1
                        k += 1

                    backtrack(i+1, placed, blocked.union(curr_blocked))

                    placed.remove((i,j))

            return


        backtrack(0, set(), set())

        res = []
        for solution in solutions:
            queens_positions = []
            for i in range(n):
                pos = "." * n
                for j in range(n):
                    if (i, j) in solution:
                        queen_pos = pos[:j] + "Q" + pos[j+1:]

                queens_positions.append(queen_pos)

            res.append(queens_positions)

        return res
