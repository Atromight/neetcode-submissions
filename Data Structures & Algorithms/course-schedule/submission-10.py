class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for _ in range(numCourses)]
        for src, dest in prerequisites:
            edges[src].append(dest)

        print(f"edges: {edges}")
        for i in range(numCourses):
            print("")
            print(f"i: {i}, edges: {edges[i]}")
            if edges[i]:
                q = deque([])
                q.append([i, set()])
                while q:
                    # print(f"q: {q}")
                    src, curr_v = q.popleft()
                    for dest in edges[src]:
                        if dest in curr_v:
                            # print(f"src: {src}, edges: {edges[src]}, dest: {dest}, curr_v: {curr_v}")
                            return False

                        curr_v.add(src)
                        q.append([dest, curr_v.copy()])

        return True
