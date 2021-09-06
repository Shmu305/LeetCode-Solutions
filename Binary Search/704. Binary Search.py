class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = left + (right - left)// 2
            if nums[pivot] == target:
                return pivot
            else:
                if nums[pivot] < target:
                    left = pivot + 1
                if nums[pivot] > target:
                    right = pivot - 1
        return -1
        
