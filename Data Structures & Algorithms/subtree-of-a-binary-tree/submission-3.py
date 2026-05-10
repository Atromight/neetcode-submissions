# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        is_sub = False
        stack = [root]
        traversed = set()
        while stack and not is_sub:
            curr = stack[-1]
            if curr.left and curr.left not in traversed:
                stack.append(curr.left)
            elif curr.right and curr.right not in traversed:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                sub = subRoot

                if curr.val == sub.val:
                    is_sub = self.traverseTree(curr, sub)

                traversed.add(curr)

        return is_sub


    def traverseTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and not root:
            return True

        if not root:
            return False

        if root and subRoot and root.val == subRoot.val:
            return (
                self.traverseTree(root.left, subRoot.left) and
                self.traverseTree(root.right, subRoot.right)
            )
        else:
            return False
