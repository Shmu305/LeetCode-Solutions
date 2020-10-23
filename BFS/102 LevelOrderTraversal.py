# O(n) time
# O(n) space on the queue
class Solution(object):
    def levelOrder(self, root):
        result = []
        q = deque()
        if root:
            q.append(root)
        while q:
            curLevel = []
            for i in range(len(q)):
                node = q.popleft()
                curLevel.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            result.append(curLevel)
        return result
