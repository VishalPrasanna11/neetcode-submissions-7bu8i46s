class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)

        heap = []

        for num, value in countMap.items():
            heapq.heappush(heap, (value,num))
            if len(heap) >k:
                heapq.heappop(heap)


        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
