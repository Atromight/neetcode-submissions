import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt_map = {}
        for task in tasks:
            cnt_map[task] = cnt_map.get(task, 0) + 1

        heap = []
        heapq.heapify(heap)
        for task in cnt_map:
            heapq.heappush(heap, [-cnt_map[task], task])


        cycle = 0
        queue = deque() # pairs of [-cnt, next_cycle]
        while heap or queue:
            cycle += 1

            if not heap:
                cycle = queue[0][1]
            else:
                cnt, task = heapq.heappop(heap)
                cnt = -cnt
                cnt -= 1
                if cnt > 0: # We will have to complete another task of type t in the future
                    queue.append([-cnt, cycle + n, task])

            if queue and queue[0][1] == cycle:
                cnt, nxt_cycle, task = queue.popleft()
                heapq.heappush(heap, [cnt, task])

        return cycle
