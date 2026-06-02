class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vertix_map = [[] for _ in range(n)]
        for src, dest in edges:
            vertix_map[src].append(dest)
            vertix_map[dest].append(src)

        res = 0
        visited = set()       
        for i in range(n):
            if i in visited:
                continue

            visited.add(i)
            if vertix_map[i]:
                q = deque([])
                q.append(i)
                while q:
                    src = q.popleft()
                    for dest in vertix_map[src]:
                        if dest not in visited:
                            visited.add(dest)
                            q.append(dest)

            res += 1

        return res
