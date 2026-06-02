class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for _ in range(numCourses)]
        for src, dest in prerequisites:
            edges[src].append(dest)

        for i in range(numCourses):
            if edges[i]:
                q = deque([])
                q.append([i, set()])
                while q:
                    src, curr_v = q.popleft()
                    for dest in edges[src]:
                        if dest in curr_v:
                            return False

                        curr_v.add(src)
                        q.append([dest, curr_v.copy()])

        return True
