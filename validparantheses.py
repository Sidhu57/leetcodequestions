class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hs = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in hs:         
                stack.append(c)
            else:                   
                if not stack:      
                    return False
                popped = stack.pop()
                if popped != hs[c]: 
                    return False

        return not stack            
s1 = Solution()
print(s1.isValid("(){}[]"))  
print(s1.isValid("()")) 
print(s1.isValid("[}"))  

