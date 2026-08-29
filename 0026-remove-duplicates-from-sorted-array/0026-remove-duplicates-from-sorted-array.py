class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        i=0
        j=1
        k=1
        while j<n:
            if nums[j]==nums[i]:
                j+=1
                continue
            nums[i+1]=nums[j]
            i+=1
            j+=1
            k+=1
        return k

