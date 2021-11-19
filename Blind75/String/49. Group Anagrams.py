#Time: O(m*n) each string (M) * avg length (N) is iterated once
#Space:O(n) size of map
class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            if tuple(key) in res:
                res[tuple(key)].append(s)
            else:
                res[tuple(key)] = [s]

        return res.values()
