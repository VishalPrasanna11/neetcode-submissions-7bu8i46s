class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        goal = len(nums)//2

        hashMap = {}

        for num in nums:
            hashMap[num] = 1+ hashMap.get(num,0)

            if hashMap[num] >goal:
                return num