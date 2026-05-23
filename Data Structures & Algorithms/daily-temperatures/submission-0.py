class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackIdx, stackTemp = stack.pop()
                res[stackIdx] = (i - stackIdx)
            stack.append((i,t))
        return res