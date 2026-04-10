class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        flag = False
        zero_count = 0  # To count the number of zeros in the list
        for num in nums:
            if num != 0:
                total *= num
            else:
                zero_count += 1
        
        if zero_count > 1:  # If there are more than one zero, the result is all zeros
            return [0] * len(nums)
        
        i = 0
        for num in nums:
            if zero_count == 1:  # If there's exactly one zero, the result is zero except for that index
                if num == 0:
                    nums[i] = total
                else:
                    nums[i] = 0
            else:  # No zeros, proceed with the division
                nums[i] = total // num
            i += 1
        
        return nums
