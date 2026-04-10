class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        n = len(height)
        maxLeft = [0]*n
        maxLeft[0] = height[0]

        for i in range(1,n):
            maxLeft[i] = max(maxLeft[i-1],height[i])
        
        maxRight = [0]*n
        maxRight[n-1] = height[n-1]

        for i in range(n-2,-1,-1):
            maxRight[i] = max(maxRight[i+1], height[i])

        total = 0

        for i in range(n):
            water_level = min(maxLeft[i], maxRight[i])

            waterTrap = max(0, water_level-height[i])

            total += waterTrap


        return total
        