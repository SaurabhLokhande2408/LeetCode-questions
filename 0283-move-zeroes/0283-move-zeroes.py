class Solution(object):
    def moveZeroes(self, nums):
        for num in nums:
            if num==0:
                nums.pop(nums.index(num))
                nums.append(0)
            