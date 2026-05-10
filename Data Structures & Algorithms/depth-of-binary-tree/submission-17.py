# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Recursive
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        #Iterative
        if not root:
            return 0
        queue = deque([(root, 0)])
        
        while queue:
            for i in range(len(queue)):
                node, level = queue.popleft()
                
                if node:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))
        return level
                

        

        