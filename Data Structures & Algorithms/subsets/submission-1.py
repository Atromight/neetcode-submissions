class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = self.generate_subsets(nums, [set(nums)])
        return [list(s) for s in subsets]
        
    def generate_subsets(
        self,
        remaining: List[int],
        subsets: List[List[int]],
    ):
        if remaining:
            k = len(subsets)
            num = remaining.pop(0)
            i = 0
            while i < k:
                subset = subsets[i].copy()
                subset.remove(num)
                subsets.append(subset)
                i += 1

            return self.generate_subsets(remaining, subsets)
        else:
            return subsets