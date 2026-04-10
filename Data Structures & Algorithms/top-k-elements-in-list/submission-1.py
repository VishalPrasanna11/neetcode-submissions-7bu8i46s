class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num,0)

        desc_sort = sorted(hashMap.items() , key = lambda item : item[1], reverse = True)

        res = []
        for i in range(k):
            res.append(desc_sort[i][0])


        return res