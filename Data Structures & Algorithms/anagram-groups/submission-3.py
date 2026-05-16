class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result  = defaultdict(list)

        for s in strs:
            sorted_String = ''.join(sorted(s))
            result[sorted_String].append(s)
        return list(result.values())

