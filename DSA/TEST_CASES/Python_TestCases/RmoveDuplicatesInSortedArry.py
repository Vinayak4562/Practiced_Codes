class Solution:
    def removeDuplicates(self, nums):
        nums[:]=list(set(nums))
        nums.sort()
        return (len(nums))
    
A = Solution()
nums= [1,1,2,3,4,4,5,6,6,7,8]
A.removeDuplicates(nums)
# print(A.removeDuplicates(nums))
print(nums)

