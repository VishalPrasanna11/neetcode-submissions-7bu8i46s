class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        result = []

        def helper(idx, currSet, currSum):

            if currSum == target:
                result.append(currSet[:])
            
            if idx > n or currSum > target:
                return
            

            seen = set()
            for i in range(idx, n):
                if candidates[i] in seen:
                    continue
                seen.add(candidates[i])
                currSet.append(candidates[i])
                helper(i +1, currSet[:], currSum + candidates[i])
                currSet.pop()

            
        helper(0, [], 0)
        return result


    