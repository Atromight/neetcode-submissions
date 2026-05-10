# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = [root]

        while queue:
            rightmost = None
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    rightmost = node.val
                    level.append(node.left)
                    level.append(node.right)

            if rightmost is not None:
                res.append(rightmost)
            
            if level:
                for node in level:
                    queue.append(node)

        return res

                    


        