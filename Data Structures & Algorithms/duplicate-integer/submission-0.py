class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         new_array=[]

         for num in nums:
            if num in new_array:
                return True
            else: new_array.append(num)
        
         return False