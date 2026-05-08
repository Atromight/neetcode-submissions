# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same = True
        stack = [(p, q)]
        diff_map = {(None, None): 0}
        if not p and not q:
            return True

        if (
            (p and not q) or
            (q and not p)
        ):
            return False

        while stack and is_same:
            p, q = stack[-1]

            if p.left and q.left and (p.left, q.left) not in diff_map:
                stack.append((p.left, q.left))
            elif p.right and q.right and (p.right, q.right) not in diff_map:
                stack.append((p.right, q.right))
            else:
                if (
                    (p.left and not q.left) or
                    (q.left and not p.left) or
                    (p.right and not q.right) or
                    (q.right and not p.right)
                ):
                    is_same = False
                else:
                    p, q = stack.pop()

                    # diff_l = diff_map[(p.left, q.left)]
                    # diff_r = diff_map[(p.right, q.right)]
                    # if diff_l != 0 or diff_r != 0:
                    #     is_same = False

                    diff = abs(p.val - q.val)
                    if diff != 0:
                        is_same = False

                    diff_map[(p, q)] = diff

        return is_same

        