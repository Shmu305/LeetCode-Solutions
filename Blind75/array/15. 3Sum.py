# Time: O(n^2) an improvement on the O(n^3) brute force solution
# Space: O(1) maybe O(n) depending in library
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                triplet = a + nums[l] + nums[r]
                if triplet > 0:
                    r -= 1
                elif triplet < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
            
