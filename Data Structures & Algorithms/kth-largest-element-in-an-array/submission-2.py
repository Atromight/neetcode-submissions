import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        min_heap = []
        heapq.heapify(min_heap)

        for num in nums:
            if len(min_heap) == k:
                curr_min = min_heap[0]
                if curr_min < num:
                    heapq.heapreplace(min_heap, num)

            else:
                heapq.heappush(min_heap, num)

        return min_heap[0]

        