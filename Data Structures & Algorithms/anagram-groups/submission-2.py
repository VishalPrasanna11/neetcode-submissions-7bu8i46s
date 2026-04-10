class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))
            hashMap[sorted_string].append(string)

        return list(hashMap.values())