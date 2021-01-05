class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        sliding_dict = collections.Counter()
        s1_dict = collections.Counter(s1)
        for i, c in enumerate(s2):
            sliding_dict[c] += 1
            if sum(sliding_dict.values()) == len(s1):
                if s1_dict == sliding_dict:
                    return True
                left_char = s2[i - len(s1) + 1]
                if sliding_dict[left_char] == 1:
                    del sliding_dict[left_char]
                else:
                    sliding_dict[left_char] -= 1
        return False
            
