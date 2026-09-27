class Solution(object):
    def runningSum(self, nums):
        running_sum=0
        for i in range(len(nums)):
            running_sum=nums[i]+running_sum
            nums[i]=running_sum
        return nums
        