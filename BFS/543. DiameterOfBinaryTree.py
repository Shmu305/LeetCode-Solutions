class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans, 2+left+right)
            return 1 + max(left, right)
            
         
        dfs(root)
        return self.ans
