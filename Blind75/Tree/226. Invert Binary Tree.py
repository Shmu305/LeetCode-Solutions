class Solution(object):
    def invertTree(self, root):
        deq = deque()
        deq.append(root)
        while deq:
            node = deq.popleft()
            if node:
                node.left, node.right = node.right, node.left
                deq.append(node.left)
                deq.append(node.right)
        return root
      
  #recursive
    def invertTree(self, root):
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
