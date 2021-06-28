def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
   
        if not nums:
            return 0
        dic = {}
        for i, n in enumerate(nums):
            compliment = target -n
            if compliment in dic:
                return [i, dic[compliment]]
            dic[n] = i
        
