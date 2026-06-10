class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        We will need 3 for loops, 1 for each column of the triplets.
        In each for loop, the goal is to store the triplet that has
        the number that is equal to the value needed for the target triplet for that column,
        and the other 2 column vals are less than or equal to the target vals for the columns.
        If we cannot find such triplet for any of the 3 columns we return False.
        Otherwise, if we find for all 3 we return True.

        NOTE: We probably don't need 3 loops, 1 should do it.
        If for any triplet it satisfies the above requirements for any (or all) of the 3 columns
        we store it.
        In every iteration, we check if all 3 response triplets have been found.
        if we have found them we can break early and return True.

        if we finish the loop, and we haven't found them return False.
        """
        triplet_x = None
        triplet_y = None
        triplet_z = None
        for a, b, c in triplets:
            if a == target[0] and b <= target[1] and c <= target[2]:
                triplet_x = [a, b, c]

            if a <= target[0] and b == target[1] and c <= target[2]:
                triplet_y = [a, b, c]

            if a <= target[0] and b <= target[1] and c == target[2]:
                triplet_z = [a, b, c]

            if triplet_x and triplet_y and triplet_z:
                return True

        return False
