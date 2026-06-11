class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n == 1:
            return 0

        edges = {}
        for u, v, t in times:
            if u in edges:
                edges[u].add((v, t))
            else: # u not in edges
                edges[u] = set([(v, t)])

        res = [None] * n
        q = deque()
        # visited = set()

        res[k-1] = 0
        # visited.add(k)
        for v, t in edges.get(k, set()):
            res[v-1] = t
            q.append([v, t])

        while q:
            cur_v, cur_t = q.popleft()
            for v, t in edges.get(cur_v, set()):
                if (
                    (res[v-1] is not None and res[v-1] > (cur_t + t)) or
                    res[v-1] is None
                ):
                    res[v-1] = cur_t + t
                    q.append([v, cur_t + t])

        # print(f"res: {res}")
        if None in res:
            return -1

        else:
            return max(res)
