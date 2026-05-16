# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -1001
        tmp = self.largestSum(root)
        return self.max_sum


    def largestSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = self.largestSum(root.left)
        r = self.largestSum(root.right)
        l = max(l, 0)
        r = max(r, 0)
        if root.val + l + r > self.max_sum:
            self.max_sum = root.val + l + r

        return root.val + max(l, r)
        