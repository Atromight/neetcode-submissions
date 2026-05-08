class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        cnt1 = {}
        for i in range(len(s1)):
            if s1[i] in cnt1:
                cnt1[s1[i]] += 1
            else:
                cnt1[s1[i]] = 1

        i = 0
        j = 1
        cnt2 = {s2[0]: 1}
        if cnt1 == cnt2:
            return True

        while i <= j and j < n2:
            if s2[j] in cnt1:
                if s2[j] in cnt2 and cnt2[s2[j]] < cnt1[s2[j]]:
                    cnt2[s2[j]] += 1

                elif s2[j] in cnt2 and cnt2[s2[j]] == cnt1[s2[j]]:
                    while cnt2[s2[j]] == cnt1[s2[j]]:
                        cnt2[s2[i]] -= 1
                        i += 1

                    cnt2[s2[j]] += 1

                elif s2[j] not in cnt2:
                    cnt2[s2[j]] = 1

            else:
                cnt2 = {}

            if cnt1 == cnt2:
                return True

            if s2[j] not in cnt1:
                cnt2 = {}
                j += 1
                i = j
            else:
                j += 1

        return False

