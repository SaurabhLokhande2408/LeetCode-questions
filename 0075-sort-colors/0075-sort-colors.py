class Solution(object):
    def sortColors(self, nums):
        zero = 0
        one = 0
        two = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
            else:
                two += 1

        nums[:]= []

        for zeros in range(zero):
            nums.append(0)

        for ones in range(one):
            nums.append(1)

        for twos in range(two):
            nums.append(2)

        return nums