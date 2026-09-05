class Solution(object):
    def sortedSquares(self, nums):
        sq=[]
        nums.sort()
        for num in nums:
            sq.append(num*num)
            sq.sort()
        return sq
            
        