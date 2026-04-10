class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def helper(left,right):
            
            if left > right:
                return -1
            mid = (right+left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                return helper(mid+1,right)
            else: return helper(left,mid-1)




        return helper(0,len(nums)-1)