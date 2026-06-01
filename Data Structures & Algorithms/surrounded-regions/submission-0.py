class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = set([
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ])

        borders = set()
        for i in range(m):
            if board[i][0] == "O":
                borders.add((i, 0))

            if board[i][n-1] == "O":
                borders.add((i, n-1))

        for j in range(n):
            if board[0][j] == "O":
                borders.add((0, j))

            if board[m-1][j] == "O":
                borders.add((m-1, j))

        def dfs(
            pos: tuple[int, int],
            visited: set[tuple[int, int]]
        ) -> None:
            x, y = pos[0], pos[1]
            if (
                (x, y) in visited or
                x < 0 or y < 0 or
                x == m or y == n or
                board[x][y] == "X"
            ):
                return

            visited.add((x, y))
            for i, j in directions:
                dfs((x+i, y+j), visited)

        unchanged = set()
        for (x,y) in borders:
            dfs((x,y), unchanged)

        for i in range(m):
            for j in range(n):
                if (
                    board[i][j] == "O" and
                    (i, j) not in unchanged
                ):
                    board[i][j] = "X"
