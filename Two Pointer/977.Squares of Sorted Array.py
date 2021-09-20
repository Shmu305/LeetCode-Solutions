    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        l , r = 0 , len(nums)-1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                ans[r-l] = left*left 
                l += 1
            else:
                ans[r-l] = right*right
                r -= 1
        return ans
