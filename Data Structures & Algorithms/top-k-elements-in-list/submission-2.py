class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # S : O(N)
        # hashMap = {}

        # # T : O(N)
        # for num in nums:
        #     hashMap[num] = 1 + hashMap.get(num,0)

        # # S : O(nlogn)
        # desc_sort = sorted(hashMap.items() , key = lambda item : item[1], reverse = True)

        # # S: O(K)
        # res = []
        # # T : O(k)
        # for i in range(k):
        #     res.append(desc_sort[i][0])


        # return res

        # #Final
        # #T : O(n+k) + O(nlogn) = O(nlogn)
        # # S: O(n+k) = O(n)

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        heap = []

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        
        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt,num])
        
        # arr.sort()

        # res  = []

        # while len(res) < k:
        #     res.append(arr.pop()[1])
        
        # return res

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res