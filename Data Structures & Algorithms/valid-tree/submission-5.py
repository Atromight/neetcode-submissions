class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        vertix_map = [[] for _ in range(n)]
        for src, dest in edges:
            print(f"src: {src}, dest: {dest}")
            if src == dest:
                return False

            vertix_map[src].append(dest)
            vertix_map[dest].append(src)
        
        if n == 1:
            return True

        print(f"vertix_map: {vertix_map}")
        for i in range(n):
            visited = set()
            if vertix_map[i]:
                q = deque([])
                q.append([i, None, set()])
                while q:
                    src, prev, curr_v = q.popleft()
                    for dest in vertix_map[src]:
                        if dest == prev:
                            continue

                        else:
                            if dest in curr_v:
                                print(f"src: {src}, dest: {dest}, prev: {prev}, curr_v: {curr_v}")
                                return False

                        curr_v.add(src)
                        q.append([dest, src, curr_v.copy()])
                    
                    visited.add(src)

                if len(visited) != n:
                    return False

            else:
                return False

        return True
