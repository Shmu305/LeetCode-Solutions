#recursive solution ------------------------

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or q.val != p.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
--------------------------------------------------   
#iterative solution 
        
class Solution(object):
    def isSameTree(self, p, q):
        deq = deque()
        deq.append((p, q))
        while deq:
            p, q = deq.popleft()
            if not p and not q:
                continue
            if not p or not q or q.val != p.val:
                return False
            deq.append((p.left, q.left))
            deq.append((p.right, q.right))
        return True
            
      
