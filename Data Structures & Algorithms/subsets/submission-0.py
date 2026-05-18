class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = self.generate_subsets(nums, [set(nums)])
        print(subsets)
        return [list(s) for s in subsets]
        
    def generate_subsets(
        self,
        remaining: List[int],
        subsets: List[List[int]],
    ):
        print("remaining: ", remaining)
        # print("subsets: ", subsets)
        if remaining:
            k = len(subsets)
            num = remaining.pop(0)
            i = 0
            while i < k:
                subset = subsets[i].copy()
                subset.remove(num)
                # print(subsets)
                subsets.append(subset)
                # print(subsets)
                i += 1

            return self.generate_subsets(remaining, subsets)
        else:
            return subsets