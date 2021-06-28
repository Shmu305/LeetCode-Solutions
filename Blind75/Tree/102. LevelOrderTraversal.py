def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        q = deque()
        if root:
            q.append(root)
        while q:
            curLevel = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                curLevel.append(node.val)
            result.append(curLevel)
        return result
