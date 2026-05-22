class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cnt = {}
        unique = set()
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
            if num not in unique:
                unique.add(num)

        nums_unique = list(unique)
        n = len(nums_unique)

        def backtrack(i: int, cur: List[int], cnt: dict[int, int]):
            if i == n:
                return

            num = nums_unique[i]
            if cnt[num] > 0:
                cnt[num] -= 1
                cur.append(num)

                backtrack(i, cur, cnt)

                res.append(cur.copy())
                cur.pop()
                cnt[num] += 1

                backtrack(i+1, cur, cnt)

            else:  
                backtrack(i+1, cur, cnt)

            return


        backtrack(0, [], cnt)
        res.append([])

        return res








