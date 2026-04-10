class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        leftProd = 1
        rightProd = 1
        ans = nums[0]
        n = len(nums)

        for i in range(n):

            leftProd = 1 if leftProd == 0 else leftProd
            rightProd = 1 if rightProd == 0 else rightProd

            leftProd *= nums[i]
            rightProd *= nums[n-i-1]

            ans = max(ans,max(leftProd,rightProd))


        return ans
