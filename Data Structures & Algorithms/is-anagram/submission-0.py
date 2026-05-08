class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            freq_map_s = {}
            freq_map_t = {}
            for i in range(0, len(s)):
                if s[i] in freq_map_s:
                    freq_map_s[s[i]] += 1
                else:
                    freq_map_s[s[i]] = 1
                
                if t[i] in freq_map_t:
                    freq_map_t[t[i]] += 1
                else:
                    freq_map_t[t[i]] = 1
                
            if freq_map_s == freq_map_t:
                return True
            else:
                return False

        else:
            return False
        