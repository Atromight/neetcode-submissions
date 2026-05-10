# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 1
        curr_max = root.val
        
        self.traverseTree(root.left, curr_max)
        self.traverseTree(root.right, curr_max)

        return self.res


    def traverseTree(self, root: TreeNode, curr_max: int):
        if root is None:
            return
        
        if root.val >= curr_max:
            self.res += 1
            curr_max = root.val

        self.traverseTree(root.left, curr_max)
        self.traverseTree(root.right, curr_max)

        return
