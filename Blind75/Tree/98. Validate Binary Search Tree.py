class Solution(object):
    def isValidBST(self, root):
        
        def isValid(node, left, right):
            if not node:
                return True
            if not(node.val > left and node.val < right):
                return False
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        return isValid(root, float("-inf"), float("inf"))
            
