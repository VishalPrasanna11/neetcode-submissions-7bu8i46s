class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        elif len(s) ==1:
            return 1

        
        left = 0
        right =1
        max_length =1
        char_list=set()
        for right in range(len(s)):
            
            while s[right] in char_list:
                char_list.remove(s[left])
                left+=1
            
            char_list.add(s[right])

            max_length=max(max_length,right-left+1)

        return max_length


