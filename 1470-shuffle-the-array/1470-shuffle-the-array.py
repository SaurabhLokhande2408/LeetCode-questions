class Solution(object):
    def shuffle(self, nums, n):
        temp=nums[n:]
        del nums[n:]
        for i in range(n):
            nums.insert(i*2 +1,temp[i])
        return nums

        