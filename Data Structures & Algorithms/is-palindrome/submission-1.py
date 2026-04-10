class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = ''.join(ch.lower() for ch in s if ch.isalnum())
        n = len(sc)

        l = 0
        r = n-1

        while l < r:

            if sc[l] == sc[r]:
                l+=1
                r -=1
            else:
                return False

        return True