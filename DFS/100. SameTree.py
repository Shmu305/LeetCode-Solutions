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
