class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        for i in range(len(nums)-k+1):
            cur_max = float('-inf') 
            for j in range(k):
                cur_max = max(cur_max,nums[i+j])
            output.append(cur_max)

        return output