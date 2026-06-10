class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        First I iterate through the string and I create a dictionary.
        For every letter I encounter, I store 2 positions: the first
        occurence and the last occurence of it.
        Then, I iterate through the string again and
        for each letter I encounter:
        i. If the current pos is between the start/end range,
                I update the start/end range.
        ii. If the current pos is the same as the end, I store
                the length of the current substring
        iii. If the current pos is larger than the end, a new
                substring begins. Thus, I have to initialize a new j
                (j is the starting position for the new substring which
                I use to determine the length of it once I reach the end of it).
                I also handle the edge case of a letter being it's own substring.
        """
        n = len(s)
        if n == 1:
            return [1]

        letter_pos = {}
        for i in range(n):
            letter = s[i]
            if s[i] not in letter_pos:
                letter_pos[letter] = [i, i]
            else:
                letter_pos[letter][1] = i

        res = []
        prev_start, prev_end = letter_pos[s[0]]
        j = 0
        i = 0
        while i < n:
            letter = s[i]
            start, end = letter_pos[letter]
            if i < prev_end:
                start = min(start, prev_start)
                end = max(end, prev_end)

            elif i == prev_end:
                # Substring ends here
                res.append(i - j + 1)

            else: # i > prev_end
                # New substring starts here
                j = i
                if start == end:
                    res.append(1)

            prev_start = start
            prev_end = end
            i += 1

        return res
