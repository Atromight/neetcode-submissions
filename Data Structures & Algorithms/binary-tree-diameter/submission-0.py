# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.diameter = 0
        edge = self.longestEdge(root)
        return self.diameter

    def longestEdge(self, root: Optional[TreeNode]) -> int:
        if root.left and root.right:
            l = self.longestEdge(root.left) + 1
            r = self.longestEdge(root.right) + 1
            if l + r > self.diameter:
                self.diameter = l + r

            return max(l, r)

        elif root.left:
            l = self.longestEdge(root.left) + 1
            if l > self.diameter:
                self.diameter = l

            return l

        elif root.right:
            r = self.longestEdge(root.right) + 1
            if r > self.diameter:
                self.diameter = r

            return r

        elif not root.left and not root.right:
            return 0
