        if root == None:
            return 0
        q = collections.deque()
        q.append((root, 1))
        
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
                
#another way
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque()
        if root:
            q.append(root)
        minDepth = 0
        while q:
            minDepth += 1
            for i in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return minDepth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return minDepth
            
