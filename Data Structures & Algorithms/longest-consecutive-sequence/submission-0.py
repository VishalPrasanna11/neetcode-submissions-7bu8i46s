class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
      hashMap = {num : False for num in nums}
      

      if len(nums)==0:
        return 0
      elif  len(nums)==1:
        return 1
      
      longest = 1
      
      for num in nums:

        curr=1
        nextNum = num+1

        while(nextNum in hashMap and hashMap[nextNum]==False):
            curr+=1
            hashMap[nextNum]=True
            nextNum+=1
        
        preNum= num-1

      
        while(preNum in hashMap and hashMap[preNum]==False):
            curr+=1
            hashMap[preNum]=True
            preNum-=1
        
        if(longest<curr):
            longest = curr
      

      return longest
