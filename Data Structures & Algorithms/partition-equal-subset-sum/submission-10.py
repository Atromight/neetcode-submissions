class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        print(f"sum(nums): {sum(nums)}")
        # If sum of all nums cannot be split into 2 integers,
        # then the 2 equal integers sums cannot be formed either.
        if s % 2 != 0:
            return False

        visited = set()
        t = s // 2
        q = deque()
        q.append([0, 0])
        while q:
            i, sum1 = q.popleft()
            if sum1 == t:
                return True

            if i == n or sum1 > t:
                continue

            if (i, sum1) not in visited:
                q.append([i+1, sum1 + nums[i]])
                visited.add((i, sum1))

            q.append((i+1, sum1))

        return False
