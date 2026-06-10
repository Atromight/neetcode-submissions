class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        hand.sort()
        freq = {}
        for val in hand:
            if val in freq:
                freq[val] -= 1
                if freq[val] == 0:
                    freq.pop(val)

            else:
                for i in range(1, groupSize):
                    freq[val + i] = freq.get(val + i, 0) + 1
        
        if freq:
            return False
        else:
            return True

