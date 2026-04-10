class Solution:
    def search(self, nums: List[int], target: int) -> int:


        def helper(left,right):

            if left>right:
                return -1

            mid = (right+left)//2
            match = nums[mid]
            leftnum = nums[left]
            rightnum = nums[right]
            if nums[mid] == target:
                return mid
            elif leftnum <= match:
                if target<match and target >= leftnum:
                    return helper(left,mid-1)
                else:
                    return helper(mid+1,right)
            else:
                if target>match and target <= rightnum:
                    return helper(mid+1,right)
                else: return helper(left, mid-1)
            



        return helper(0,len(nums)-1)
        