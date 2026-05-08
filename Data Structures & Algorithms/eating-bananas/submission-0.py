import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = max(piles) # O(n)
        # min_k = m

        l = 1
        r = m
        while l <= r:
            k = (l + r) // 2
            h_left = h
            run_out = False
            for i in range(n):
                pile = piles[i]
                h_left -= math.ceil(pile/k)
                if h_left < 0 :
                    run_out = True
                    break

            if run_out == True:
                if r - l == 1:
                    l = r
                else:
                    l = k

            else: # run_out == False
                if l == r:
                    return k
                else:
                    r = k


                



        