        if not p and not q:
            return True
        if not p or not q:
            return False
        else:
            return (p.val ==q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(q.right, p.right) 
