class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        n = len(word1)
        m = len(word2)
        res = []
        while l < n and r < m:
            res.append(word1[l] + word2[r]) 
            l += 1
            r += 1


        if l < n:
            res.append(word1[l:])
        
        if r < m:
            res.append(word2[r:])


        return "".join(res)