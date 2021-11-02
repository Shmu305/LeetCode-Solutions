class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res =  nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            #find out if there's a sorted subarray
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            m = (l+r)//2
            res = min(res, nums[m])
                
            #find out if m is located in the left half of the rotation
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return res
                
