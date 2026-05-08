class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        unique_freq_maps = set()
        for s in strs:
            new_anagram = True
            if groups:
                for group in groups:
                    if self.isAnagram(s, group[0]):
                        group.append(s)
                        new_anagram = False

                if new_anagram == True:
                    groups.append([s])
                
            # first string
            else:
                groups.append([s])
        
        return groups

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
        