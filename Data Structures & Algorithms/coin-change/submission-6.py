class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort()
        self.res = amount + 1

        def dfs(i: int, rem: int, m: int) -> None:
            if i < 0:
                return

            val = coins[i]
            div = rem // val
            mod = rem % val
            while div >= 0:
                if mod == 0:
                    cur = m + div
                    if cur < self.res:
                        self.res = cur
                        return

                else:
                    dfs(i-1, mod, m + div)

                div -= 1
                mod += val

            return

        dfs(n-1, amount, 0)

        if self.res > amount:
            return -1

        return self.res
