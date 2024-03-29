class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        curMax, curMin = 1, 1
        
        for n in nums:
            tmp = n*curMax
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax)
        return res
            
