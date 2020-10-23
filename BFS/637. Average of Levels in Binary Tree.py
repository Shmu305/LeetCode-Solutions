Time: O(n) to traverse entire tree
Space; O(m) where m is the max size of queue at any given level

class Solution(object):
    def averageOfLevels(self, root):
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
            result.append(sum(curLevel)*1.0/len(curLevel))
        return result
        
