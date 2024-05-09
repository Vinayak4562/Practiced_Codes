class Solution:
    def merge(self, nums1, m: int, nums2, n):
       
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

# nums1 = [ 1,3,5,7,9]
# nums2 = [2,4,8,9]
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
M = Solution()
print(M.merge(nums1, m,nums2,n))