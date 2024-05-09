class Solution:
   
    def search(self, nums, target ):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1
    
nums =[-1,2,4,5,6,7,8]
S = Solution()
print(S.search(nums,4))
print(S.search(nums,0))
print(S.search(nums,8))
print(S.search(nums,10))