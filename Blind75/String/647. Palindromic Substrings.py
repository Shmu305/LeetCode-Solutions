class Solution(object):
    def countSubstrings(self, s):
        res = 0
        #odd
        for i in range(len(s)):
            l, r = i, i
            while l>=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        #even
            l, r = i, i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
      
      #more concise
    def countSubstrings(self, s):
        res = 0
        for i in range(len(s)):
            #odd
            res += self.countPalindromes(s, i, i)
            #even
            res += self.countPalindromes(s, i, i+1)
        return res
    
    def countPalindromes(self, s, l, r):
        res = 0
        while l>=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
            
