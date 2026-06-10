class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        The idea is that, if the response is True, then for every number we encounter,
        it's either going to be: 
        i. the beginning of straight of size groupSize
        (so we expect to see the next groupSize -1 numbers), 
        ii. or it's already part of a previously starting straight.

        So we sort the values.
        Then whenever we encounter a value:

        If it's the first time (not in frequency dict)
        then we add the next (groupSize - 1) numbers to the frequency dictionary

        If we have already encountered a number before (it's in frequency dict)
        then we decrease count by 1 (and if it's 0 then we remove it from the dict altogether).

        That way by the end, if the response is True the dict will be empty,
        or not empty otherwise (response is False).
        """
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
