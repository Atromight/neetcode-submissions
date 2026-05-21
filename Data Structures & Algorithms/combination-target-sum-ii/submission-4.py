class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(i: int, curr_l: List[int], curr_sum: int):
            if curr_sum == target:
                res.append(curr_l.copy())
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if curr_sum > target:
                    return

                curr_l.append(candidates[j])
                curr_sum += candidates[j]           
                dfs(j+1, curr_l, curr_sum)
                curr_l.pop()
                curr_sum -= candidates[j]


        dfs(0, [], 0)

        return res
        