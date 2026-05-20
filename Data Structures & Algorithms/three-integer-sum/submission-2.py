class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        n = len(nums)
        nums.sort()

        result = []

        for i in range(n - 2):
            
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left = i + 1
            right = n - 1
            total = 0
            while left < right:
                total = nums[left] + nums[i] + nums[right]

                if total == 0:
                    result.append([nums[left],nums[i],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1

                elif total < 0:
                    left += 1
                else : 
                    right -= 1


        return result