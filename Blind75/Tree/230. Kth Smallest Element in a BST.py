class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        while root or stack:
            while root:
                root = root.left
                stack.append(root)
        
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
