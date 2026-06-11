class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        First, I create a dictionary edges = {u_i: set((v_i, t_i))}
        where u_i is the source vertix
        and v_i are the destination vertices plus the time to get there.
        Then, I create a res array which stores the min time to arrive
        to each vertix i
        Finally I do a BFS traversal where for every vertix,
        I see if I have already traversed its destinations
        and if I have I check whether the time to get there
        is less this time.
        """
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

        res[k-1] = 0
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

        if None in res:
            return -1

        else:
            return max(res)
