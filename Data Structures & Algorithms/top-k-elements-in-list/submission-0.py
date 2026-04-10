class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}

        for num in nums:
            hashMap[num]= hashMap.get(num,0)+1
        
        sorted_dict = sorted(hashMap.items(), key=lambda item: item[1], reverse = True)
            
        ans = [item[0] for item in sorted_dict[:k]]
        return ans