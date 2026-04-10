class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        new_array ={}

      

        for i in range(len(nums)):
            diff = target- nums[i]

            if diff in new_array:
                return [new_array[diff],i]
            new_array[nums[i]] = i

        return []


        