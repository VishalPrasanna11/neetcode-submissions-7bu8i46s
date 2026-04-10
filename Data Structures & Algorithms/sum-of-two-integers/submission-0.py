class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to get 32 bits
        mask = 0xFFFFFFFF
        
        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask
        
        # If a is greater than 2**31 - 1, it's a negative number in 32-bit
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
