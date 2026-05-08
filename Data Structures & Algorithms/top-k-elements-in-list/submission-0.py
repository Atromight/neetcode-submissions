class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        top = []
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        while k > 0:
            max_num = 0
            max_freq = 0
            for num, freq in freq_map.items():
                if freq > max_freq:
                    max_freq = freq
                    max_num = num

            top.append(max_num)
            freq_map.pop(max_num)
            k -= 1
        
        return top

            


        