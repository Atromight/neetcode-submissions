class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for edge in edges:
            edge[0] = edge[0] - 1
            edge[1] = edge[1] - 1

        print(edges)
        n = len(edges)
        vertix_map = [[] for _ in range(n)]
        for src, dest in edges:
            vertix_map[src].append(dest)
            vertix_map[dest].append(src)

        self.res = None
        def dfs(src: int, prev: int, visited: list[int]) -> None:
            print(f"Entering src: {src}, prev: {prev}, visited: {visited}, ")
            for dest in vertix_map[src]:
                if dest == prev:
                    continue
                
                if dest in visited:
                    print(f"CYCLE DETECTED !!!!!!!!!!!!!!!!")
                    idx = -1
                    for i in range(len(visited)):
                        if visited[i] == dest:
                            idx = i
                            break
                    
                    print(f"visited: {visited}, src: {src}")
                    visited = visited[idx:] + [src]
                    print(f"visited: {visited}")
                    for i in range(n-1, -1, -1):
                        edge = edges[i]
                        if edge[0] in visited and edge[1] in visited:
                            visited = list(visited)
                            self.res = [edge[0] + 1, edge[1] + 1]
                            return
                            # break

                if self.res is not None:
                    return

                visited.append(src)
                dfs(dest, src, visited.copy())
                visited.pop()

                if self.res is not None:
                    return

            return

        dfs(0, None, [])

        return self.res


        


        # for i in range(n):
        #     # visited = set()
        #     if vertix_map[i]:
        #         q = deque([])
        #         q.append([i, None, []])
        #         while q:
        #             src, prev, curr_v = q.popleft()
        #             for dest in vertix_map[src]:
        #                 if dest == prev:
        #                     continue

        #                 else:
        #                     # We found the cycle
        #                     if dest in curr_v:
        #                         for idx in range(n-1, -1, -1):
        #                             edge = edges[idx]
        #                             if edge[0] in curr_v and edge[]

        #                 curr_v.append(src)
        #                 q.append([dest, src, curr_v.copy()])
