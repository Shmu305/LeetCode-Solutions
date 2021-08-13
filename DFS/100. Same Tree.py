        if not p and not q:
            return True
        if not p or not q:
            return False
        else:
            return (p.val ==q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(q.right, p.right) 

#iterative BFS
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        deq = collections.deque()
        deq.append((p, q))
        while deq:
            p, q = deq.popleft()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False

            deq.append((p.left, q.left))
       
            deq.append((p.right, q.right))
        return True
