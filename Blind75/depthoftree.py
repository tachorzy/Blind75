'''
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
# Tree node definition

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive solution

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        return max(leftHeight, rightHeight) + 1