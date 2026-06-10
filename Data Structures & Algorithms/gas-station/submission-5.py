class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
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
