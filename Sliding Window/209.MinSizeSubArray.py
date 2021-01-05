class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = len(nums) + 1
        l = curSum = 0
        for r, num in enumerate(nums):
            if curSum < s:
                curSum += num
            while curSum >= s:
                ans = min(ans, r-l+1)
                curSum -= nums[l]
                l += 1
        return ans if ans <= len(nums)  else 0
