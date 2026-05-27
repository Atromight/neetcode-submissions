class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # I have to multiply by -1 to turn min heap into max heap
        # (Python doesn't support max heap outright)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            max1 = heapq.heappop(max_heap)
            max2 = heapq.heappop(max_heap)
            # I have to revert to positive integers
            max1 = -max1
            max2 = -max2
            val = max1 - max2
            # I add - val to revert to negative and preserve the max heap property
            heapq.heappush(max_heap, -val)
        
        max1 = heapq.heappop(max_heap)
        # I have to revert to positive before returning val
        return -max1
        