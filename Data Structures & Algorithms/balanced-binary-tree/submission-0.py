# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        is_balanced = True
        stack = [root]
        height_map = {None: 0}
        if not root:
            return True

        while stack and is_balanced:
            node = stack[-1]

            if node.left and node.left not in height_map:
                stack.append(node.left)
            elif node.right and node.right not in height_map:
                stack.append(node.right)
            else:
                node = stack.pop()

                height_l = height_map[node.left]
                height_r = height_map[node.right]
                if abs(height_l - height_r) > 1:
                    is_balanced = False

                height_map[node] = (
                    1 + max(height_l, height_r)
                )

        return is_balanced
