class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if n < m:
            return ""

        if m == 1:
            if n == 1 and s == t:
                return s
            elif n > 1:
                if t in s:
                    return t

        cnt_t = {}
        for letter in t:
            cnt_t[letter] = cnt_t.get(letter, 0) + 1

        i = 0
        j = 1
        len_shortest = n
        i_j_shortest = None
        cnt_s = {}
        pos = []
        if s[0] in cnt_t:
            cnt_s[s[0]] = 1
            pos.append(0)

        while i <= j and j < n:
            if s[j] in cnt_t:
                pos.append(j)
                if s[j] in cnt_s:
                    cnt_s[s[j]] += 1
                else:
                    cnt_s[s[j]] = 1

                while self.are_counts_at_least_equal(cnt_t, cnt_s):
                    if len_shortest >= pos[-1] - pos[0] + 1:
                        len_shortest = pos[-1] - pos[0] + 1
                        i_j_shortest = [pos[0], pos[-1]]

                    i = pos.pop(0)
                    cnt_s[s[i]] -= 1

            j += 1

        if i_j_shortest:
            res = ""
            for i in range(i_j_shortest[0], i_j_shortest[1] + 1):
                res += s[i]

            return res
        else:
            return ""


    def are_counts_at_least_equal(
        self,
        cnt1: dict,
        cnt2: dict
    ) -> bool:
        for letter in cnt1:
            if cnt2.get(letter, 0) < cnt1[letter]:
                return False

        return True

