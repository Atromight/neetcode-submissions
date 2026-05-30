"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.visited = set()
        self.traverseGraph(node)

        self.V = len(self.visited)
        self.edges = [[] for _ in range(self.V)]
        self.visited = set()
        self.generateEdges(node)

        self.nodes = [Node()] * self.V
        self.visited = set()
        return self.generateNode(1)

    
    def traverseGraph(self, node: Optional['Node']) -> None:
        if node and node.val not in self.visited:
            self.visited.add(node.val)
            for neighbor in node.neighbors:
                self.traverseGraph(neighbor)

        return


    def generateEdges(self, node: Optional['Node']) -> None:
        if node and node.val not in self.visited:
            self.visited.add(node.val)
            for neighbor in node.neighbors:
                self.edges[node.val - 1].append(neighbor.val)
                self.generateEdges(neighbor)

        return


    def generateNode(self, i: int) -> Optional['Node']:
        if i not in self.visited:
            self.visited.add(i)
            node = Node(i)
            self.nodes[i-1] = node
            for destination in self.edges[i-1]:
                node.neighbors.append(
                    self.generateNode(destination)
                )

        return self.nodes[i-1]


