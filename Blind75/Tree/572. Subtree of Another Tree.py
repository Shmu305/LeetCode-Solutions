class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSame(self, p, q):
        if not p and not q:
            return True
        if p and q:
            return p.val ==q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
