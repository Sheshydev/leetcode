# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root) + 1

    def helper(self, root):
        if not root:
            return -1
        
        lres = self.helper(root.left)
        rres = self.helper(root.right)

        return 1 + max(lres, rres)