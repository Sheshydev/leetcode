from functools import reduce

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lcm = None
        self.helper(root, p, q)
        return self.lcm

    def helper(self, root, p, q):

        if root is None:
            return False

        mres = True if root.val in [p.val, q.val] else False
        lres = self.helper(root.left, p, q)
        rres = self.helper(root.right, p, q)
        
        res = reduce(lambda x, y : x + y, [mres, lres, rres])
        if res > 1:
            self.lcm = root
        
        return mres or lres or rres
    
TreeNode