class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        This is basically a Maximum Subarray Greedy algorithm problem.
        The idea is because there is at most 1 solution (so at most 1 starting point)
        The starting point (if it exists) will be the pos where the maximum subarray starts.
        So the 1st loop (for loop) does that.
        Then, the 2nd loop (while loop) does a complete run through the list from that starting pos
        and ensures that at no point do we have a negative sum of the subarray.
        (If cur sum becomes negative it means there is no solution.)
        """
        n = len(gas)
        max_sum = gas[0] - cost[0]
        cur_sum = 0
        start_pos = 0
        for i in range(n):
            rem = gas[i] - cost[i] # remaining gas
            if cur_sum < 0:
                start_pos = i
                cur_sum = 0

            cur_sum += rem
            if cur_sum > max_sum:
                max_sum = cur_sum

        j = 0
        cur_sum = 0
        while j <= n:
            if cur_sum < 0:
                return -1

            i = start_pos + j
            if i >= n:
                i = i - n

            rem = gas[i] - cost[i]
            cur_sum += rem
            j += 1

        return start_pos
