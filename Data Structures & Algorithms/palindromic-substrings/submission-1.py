class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def helper(i, j):
            if i > j:
                return True
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = True
                else:
                    dp[i][j] = helper(i + 1, j - 1)
            else:
                dp[i][j] = False
            return dp[i][j]

        # Fill dp for all substrings
        for i in range(n):
            for j in range(i, n):
                helper(i, j)

        # Count palindromic substrings
        res = 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] == True:
                    res += 1

        return res
