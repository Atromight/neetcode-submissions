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
            for dest in vertix_map[src]:
                if dest == prev:
                    continue

                # Cycle detected
                if dest in visited:
                    idx = -1
                    # Find index in visited where cycle begins
                    for i in range(len(visited)):
                        if visited[i] == dest:
                            idx = i
                            break
                    
                    # Add to cycle nodes the current on (it hasn't been added to visited yet)
                    visited = visited[idx:] + [src]
                    # Find last edge in edges to be in cycle
                    for i in range(n-1, -1, -1):
                        edge = edges[i]
                        if edge[0] in visited and edge[1] in visited:
                            visited = list(visited)
                            self.res = [edge[0] + 1, edge[1] + 1]
                            return

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

