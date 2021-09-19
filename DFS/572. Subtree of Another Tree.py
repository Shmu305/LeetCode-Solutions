class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root:
            return root == subRoot
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSame(self, r, s):
        if not r and not s:
            return True
        if not r or not s:
            return False

        return r.val == s.val and self.isSame(r.left, s.left) and self.isSame(r.right, s.right)
