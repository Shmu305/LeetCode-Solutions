#Time: O(n)
#Space: O(1)
class Solution(object):
    def maxArea(self, height):
        res = 0
        l, r = 0, len(height)-1
        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return res
            
