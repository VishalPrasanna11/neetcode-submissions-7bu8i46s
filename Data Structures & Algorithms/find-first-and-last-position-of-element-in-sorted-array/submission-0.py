class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        low = 0
        high = len(nums)-1

        while(low<=high):
            if(low>high):
                return [-1,-1]

            mid = (high+low)//2

            if nums[mid] == target:
                templeft = mid
                tempright = mid

                while templeft > 0 and nums[templeft-1] == target:
                    templeft -=1
                while tempright < len(nums)-1 and nums[tempright+1] == target:
                    tempright +=1
                return [templeft,tempright]
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid -1

        return [-1,-1]
        


        