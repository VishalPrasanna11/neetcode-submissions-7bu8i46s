class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterMap = Counter(s)

        for char in t:
            if char not in counterMap:
                return False
           
            counterMap[char] -= 1

            if counterMap[char] == 0:
                del counterMap[char]

        return not counterMap
            