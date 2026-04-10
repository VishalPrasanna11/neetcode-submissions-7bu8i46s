class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for string in strs:
            s_sorted = ''.join(sorted(string))
            hashMap[s_sorted].append(string)

        return list(hashMap.values())