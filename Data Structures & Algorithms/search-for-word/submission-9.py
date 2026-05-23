from collections import deque

from typing import Deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def backtrack(
            pos: tuple[int, int],
            seen: set[tuple[int, int]],
            remaining: Deque[str]
        ) -> bool:
            if not remaining:
                return True

            i = pos[0]
            j = pos[1]
            if i < 0 or i == n or j < 0 or j == m:
                return False

            letter = remaining.popleft()
            if pos in seen:
                remaining.appendleft(letter)
                return False

            if letter == board[i][j]:
                seen.add((i, j))

                all_cases = (
                    backtrack((i, j+1), seen, remaining) or
                    backtrack((i, j-1), seen, remaining) or
                    backtrack((i+1, j), seen, remaining) or
                    backtrack((i-1, j), seen, remaining)
                )

                seen.remove((i, j))
                if not all_cases:
                    remaining.appendleft(letter)
                    return all_cases

                else:
                    return True

            else:
                remaining.appendleft(letter)
                return False


        is_present = False
        i = 0
        j = 0
        while i < n and j < m and not is_present:
            remaining = deque(word)
            pos = (i, j)

            is_present = backtrack(pos, set(), remaining)

            j += 1
            if j == m:
                i += 1
                j = 0

        return is_present
