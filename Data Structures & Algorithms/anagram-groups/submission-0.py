class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in group_anagrams:
                group_anagrams[sorted_s] = []

            group_anagrams[sorted_s].append(s)

        return list(group_anagrams.values())


        