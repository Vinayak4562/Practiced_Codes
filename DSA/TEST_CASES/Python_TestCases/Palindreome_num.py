class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        buff = []
        while x !=0:            
            s,r =divmod(x,10)
            x = s
            buff.append(r)
        cmp = buff[:]
        buff.reverse()
        if cmp == buff:
            return True
        else:
            return False

P = Solution()
print(P.isPalindrome(121))
print(P.isPalindrome(1221))
print(P.isPalindrome(1234))
print(P.isPalindrome(2486))
print(P.isPalindrome(5252))