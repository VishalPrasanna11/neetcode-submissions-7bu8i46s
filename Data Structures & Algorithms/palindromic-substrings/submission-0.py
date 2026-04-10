class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        # Helper to check if a string is a palindrome
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        # Generate all substrings
        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j):
                    count += 1

        return count
