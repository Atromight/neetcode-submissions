class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if n == 1:
            return 0
        
        print(f"n: {n}, src: {src}, dst: {dst}, k: {k}")
        edges = [[] for _ in range(n)]
        for u, v, p in flights:
            edges[u].append([v, p])
        
        q = deque()
        stops = 0
        for vertix, price in edges[src]:
            q.append([vertix, price, stops + 1])

        cheapest = None
        visited = {}
        while q:
            v, p, s = q.popleft()
            if s-1 > k:
                continue

            else: # s-1 <= k
                if v == dst:
                    if (
                        (cheapest is None) or
                        (cheapest is not None and p < cheapest)
                    ):
                        cheapest = p

                else:
                    for nxt_v, nxt_p in edges[v]:
                        if (nxt_v, s+1) in visited and  visited[(nxt_v, s+1)] <= (nxt_p + p):
                            continue

                        visited[(nxt_v, s + 1)] = nxt_p + p
                        q.append([nxt_v, nxt_p + p, s + 1])
        
        if cheapest is None:
            return -1
        
        return cheapest
