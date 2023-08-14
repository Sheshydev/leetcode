
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self.helper(root)
        return self.diameter
        
    def helper(self, root):
        if not root:
            return -1

        lres = self.helper(root.left)
        rres = self.helper(root.right)

        self.diameter = max(self.diameter, 2 + lres + rres)
        
        return 1 + max(lres, rres)
    
sol = Solution()
t = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))
print(sol.diameterOfBinaryTree(t))