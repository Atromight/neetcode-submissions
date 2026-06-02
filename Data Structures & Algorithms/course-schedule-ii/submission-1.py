class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        regular = [[] for _ in range(numCourses)]
        reverse = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            regular[src].append(dest)
            reverse[dest].append(src)

        # This is done to ensure we don't have circles in the graph
        for i in range(numCourses):
            if regular[i]:
                q = deque([])
                q.append([i, set()])
                while q:
                    src, curr_v = q.popleft()
                    for dest in regular[src]:
                        if dest in curr_v:
                            return []

                        curr_v.add(src)
                        q.append([dest, curr_v.copy()])

        res = []
        visited = set()
        def dfs(src: int) -> None:
            if src in visited:
                return
            
            for dest in reverse[src]:
                dfs(dest)
            
            visited.add(src)
            res.append(src)
            return


        for i in range(numCourses):
            dfs(i)

        return res



