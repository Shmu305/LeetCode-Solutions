class Solution(object):
    def levelOrderBottom(self, root):
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            level = [] 
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res[::-1]
                
        
        
