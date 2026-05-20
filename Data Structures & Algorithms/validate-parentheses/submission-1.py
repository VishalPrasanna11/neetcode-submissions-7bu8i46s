class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        hashPair = { ")" : "(", "}" : "{", "]" : "["}

        for char in s:
            if char in hashPair:
                if stack and stack[-1] == hashPair[char]:
                    stack.pop()
                else: return False
            else:
                stack.append(char)

        
        return True if not stack else False