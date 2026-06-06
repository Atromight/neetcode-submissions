class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        # If sum of all nums cannot be split into 2 integers,
        # then the 2 equal integers sums cannot be formed either.
        if s % 2 != 0:
            return False

        sums = set()
        t = s // 2
        for i in range(n-1, -1, -1):
            sums2 = set()
            for j in sums:
                sums2.add(j + nums[i])
            
            sums.add(nums[i])
            sums = sums.union(sums2)
            if t in sums:
                return True
        
        return False
        
        