#Time: O(n)
#Space: O(n)
class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {")" : "(", "]": "[", "}": "{"}
        for p in s:
            if p in closeToOpen:
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False
