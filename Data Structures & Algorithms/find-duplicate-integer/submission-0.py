class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 0

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                pointer = 0
                while pointer != slow:
                    slow = nums[slow]
                    pointer = nums[pointer]

                
                return pointer