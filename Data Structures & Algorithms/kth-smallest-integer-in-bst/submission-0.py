# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        seen = set()
        i = 0

        while stack:
            node = stack[-1]
            if node.left and node.left not in seen:
                stack.append(node.left)

            elif node.right and node.right not in seen:
                stack.append(node.right)
                if node not in seen:
                    seen.add(node)
                    i += 1

            else:
                node = stack.pop()

                if node not in seen:
                    seen.add(node)
                    i += 1

            if i == k:
                return node.val
        
        
        