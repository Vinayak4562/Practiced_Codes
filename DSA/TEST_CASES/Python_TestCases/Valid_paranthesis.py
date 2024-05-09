class Solution:
    def isValid(self, s: str) -> bool:

        arr = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                arr.append(char)
            if char == ')' or char == '}' or char == ']':
                if len(arr) == 0:
                    return False
                if char == ')' and arr[len(arr) - 1] == '(':
                    arr.pop()
                elif char == '}' and arr[len(arr) - 1] == '{':
                    arr.pop()
                elif char == ']' and arr[len(arr) - 1] == '[':
                    arr.pop()
                else:
                    return False
    
        return len(arr) == 0
    

VP = Solution()

print(VP.isValid("{{[()]}}"))

print(VP.isValid("{{[(})"))
