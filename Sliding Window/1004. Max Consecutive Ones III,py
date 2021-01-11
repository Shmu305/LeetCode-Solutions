class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        l = longest = 0
        for r, num in enumerate(A):
            if num == 0:
                K -= 1
            while K < 0:
                if A[l] == 0:
                    K += 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
