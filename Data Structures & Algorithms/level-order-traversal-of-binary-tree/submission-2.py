# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        parents = [root]
        children = []
        res = []
        any_nodes_left = True
        while any_nodes_left:
            any_nodes_left = False
            curr = []
            children = []
            for parent in parents:
                if parent:
                    any_nodes_left = True
                    curr.append(parent.val)
                    if parent.left:
                        children.append(parent.left)

                    if parent.right:
                        children.append(parent.right)

                    # children.append(parent.right)
                # else:
                #     curr.append(None)
                #     children.append(None)
                #     children.append(None)

            if any_nodes_left:
                res.append(curr)
                parents = children

        return res
