# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.left and root.right:   
            temp = root.left
            root.left = root.right
            root.right = temp
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
        elif root.left:
            root.right = self.invertTree(root.left)
            root.left = None
        elif root.right:
            root.left = self.invertTree(root.right)
            root.right = None
        else: # not root.left and not root.right
            return TreeNode(root.val)

        return root