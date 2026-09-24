class Solution(object):
    def merge(self, nums1, m, nums2, n):
      nums1[:] = nums1[:m] + nums2
      #here it says first empty nums then slice it till m then merge with nums2
      nums1.sort()
